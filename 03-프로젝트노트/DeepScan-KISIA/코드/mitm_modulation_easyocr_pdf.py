import os, json, uuid, re
import easyocr, numpy as np, fitz
from mitmproxy import http
from PIL import Image
from email.parser import BytesParser
from email.policy import default

reader = easyocr.Reader(['ko','en'])

SAVE_DIR = os.path.expanduser("C:/Users/rladb/test/mitm_prompt_logs_easyocr_pdf")
os.makedirs(SAVE_DIR, exist_ok=True)

PDF_OCR_MIN_CHARS = 30
PDF_OCR_ZOOM = 2.0
MAX_PAGES = None

def _save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def _pil_from_pixmap(pix):
    mode = "RGBA" if pix.alpha else "RGB"
    return Image.frombytes(mode, [pix.width, pix.height], pix.samples)

def _easyocr_text(img_np_or_path):
    return "\n".join(reader.readtext(img_np_or_path, detail=0, paragraph=True)).strip()

def _process_pdf_bytes(pdf_bytes, src_tag="response", filename_hint=None, content_type="application/pdf"):
    pdf_id = str(uuid.uuid4())[:8]
    pdf_filename = filename_hint if filename_hint and filename_hint.lower().endswith(".pdf") else f"pdf_{pdf_id}.pdf"
    pdf_path = os.path.join(SAVE_DIR, pdf_filename)
    with open(pdf_path, "wb") as f:
        f.write(pdf_bytes)
    print(f"[✓] {src_tag} PDF 저장됨: {pdf_path}")

    pages_out, combined_text = [], ""
    method_summary = {"pdf_text": 0, "ocr": 0, "ocr_error": 0}
    try:
        doc = fitz.open("pdf", pdf_bytes)
        page_count = len(doc)
        page_iter = range(min(page_count, MAX_PAGES) if MAX_PAGES else page_count)
        mat = fitz.Matrix(PDF_OCR_ZOOM, PDF_OCR_ZOOM)

        for i in page_iter:
            page = doc[i]
            txt = page.get_text("text").strip()
            used = "pdf_text"
            if len(txt) < PDF_OCR_MIN_CHARS:
                try:
                    pix = page.get_pixmap(matrix=mat, alpha=False)
                    pil_img = _pil_from_pixmap(pix)
                    txt = _easyocr_text(np.array(pil_img))
                    used = "ocr"
                except Exception as e:
                    print(f"[!] PDF OCR 실패 (p.{i+1}):", e)
                    txt = f"[!] OCR 실패: {str(e)}"
                    used = "ocr_error"
            method_summary[used] += 1
            pages_out.append({"page": i+1, "method": used, "text": txt})
        combined_text = "\n\n".join(p["text"] for p in pages_out).strip()
    except Exception as e:
        print("[!] PDF 처리 실패:", e)
        combined_text = f"[!] PDF 처리 실패: {str(e)}"

    json_path = os.path.join(SAVE_DIR, f"{pdf_id}.json")
    _save_json(json_path, {
        "id": pdf_id,
        "filename": os.path.basename(pdf_path),
        "content_type": content_type,
        "source": src_tag,
        "page_count": len(pages_out),
        "method_summary": method_summary,
        "text": combined_text,
        "pages": pages_out
    })
    print(f"[📝] JSON 저장됨: {json_path}")
    print(f"[📄] 내용 미리보기:\n{combined_text[:500]}\n{'-'*40}")

def _handle_image_response(flow, content_type):
    ext = content_type.split("/")[-1].split(";")[0].strip()
    image_id = str(uuid.uuid4())[:8]
    image_filename = f"image_{image_id}.{ext}"
    image_path = os.path.join(SAVE_DIR, image_filename)
    with open(image_path, "wb") as f:
        f.write(flow.response.content)
    print(f"[✓] 이미지 저장됨: {image_path}")
    try:
        text = _easyocr_text(image_path)
    except Exception as e:
        print("[!] 이미지 OCR 실패:", e)
        text = f"[!] OCR 실패: {str(e)}"
    _save_json(os.path.join(SAVE_DIR, f"{image_id}.json"), {
        "id": image_id, "filename": image_filename,
        "content_type": content_type, "source": "response", "text": text
    })
    print(f"[📄] 내용 미리보기:\n{text[:300]}\n{'-'*40}")

# --- mitmproxy hooks ---

def response(flow: http.HTTPFlow):
    ct = (flow.response.headers.get("Content-Type") or "").lower()
    url = flow.request.pretty_url.lower()

    if "image/" in ct:
        _handle_image_response(flow, ct)
        return
    # 다운로드되는 PDF
    if "application/pdf" in ct or url.endswith(".pdf"):
        _process_pdf_bytes(flow.response.content, src_tag="response", filename_hint=os.path.basename(url), content_type=ct or "application/pdf")
        return

def request(flow: http.HTTPFlow):
    ct = (flow.request.headers.get("Content-Type") or "").lower()
    url = flow.request.pretty_url.lower()
    method = flow.request.method

    # 1) S3/스토리지에 바로 PUT/POST application/pdf 로 업로드되는 경우
    if method in ("POST","PUT") and "application/pdf" in ct and flow.request.raw_content:
        print(f"[→] {method} {url} (application/pdf 업로드 감지)")
        _process_pdf_bytes(flow.request.raw_content, src_tag="request", filename_hint=os.path.basename(url), content_type=ct)
        return

    # 2) multipart/form-data 에 PDF가 섞여 있는 업로드
    if method in ("POST","PUT") and "multipart/form-data" in ct and flow.request.raw_content:
        print(f"[→] {method} {url} (multipart 업로드 감지)")
        try:
            # email.parser로 multipart 바디 파싱
            fake_headers = f"Content-Type: {flow.request.headers['Content-Type']}\r\nMIME-Version: 1.0\r\n\r\n".encode()
            msg = BytesParser(policy=default).parsebytes(fake_headers + flow.request.raw_content)
            found = 0
            for part in msg.iter_attachments():
                p_ct = (part.get_content_type() or "").lower()
                disp = part.get('Content-Disposition', '')
                filename = part.get_filename() or ""
                payload = part.get_payload(decode=True)  # bytes
                if not payload:
                    continue
                is_pdf = ("application/pdf" in p_ct) or filename.lower().endswith(".pdf") or re.search(r'filename="?.+\.pdf"?', disp, re.I)
                if is_pdf:
                    found += 1
                    print(f"   └─ PDF 파트 추출: {filename or '(no-name)'}")
                    _process_pdf_bytes(payload, src_tag="request-multipart", filename_hint=filename or None, content_type=p_ct or "application/pdf")
            if found == 0:
                print("   └─ 경고: multipart에서 PDF 파트를 찾지 못함")
        except Exception as e:
            print("[!] multipart 파싱 실패:", e)
        return

    # 3) 일부 서비스는 octet-stream + filename=*.pdf 로 보냄
    if method in ("POST","PUT") and "application/octet-stream" in ct and flow.request.raw_content:
        disp = flow.request.headers.get("Content-Disposition","")
        if re.search(r'\.pdf"?$', disp, re.I) or url.endswith(".pdf"):
            print(f"[→] {method} {url} (octet-stream PDF 추정)")
            _process_pdf_bytes(flow.request.raw_content, src_tag="request-octet", filename_hint=None, content_type=ct)
            return
