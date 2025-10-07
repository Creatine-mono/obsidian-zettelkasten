from mitmproxy import http, ctx
from datetime import datetime
import json
import os
import tempfile
import mimetypes
import chardet
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

SAVE_DIR = "/Users/wonchaehee/Desktop/mitm_prompt_logs"
UPLOADS_DIR = os.path.join(SAVE_DIR, "uploads")
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(UPLOADS_DIR, exist_ok=True)

class PromptLogger:
    def request(self, flow: http.HTTPFlow):
        if flow.request.method in ("POST", "PUT"):
            content_type = flow.request.headers.get("Content-Type", "")
            if "application/json" not in content_type:
                if flow.request.host and flow.request.host.endswith("oaiusercontent.com"):
                    file_id = flow.request.path.split("?")[0].lstrip("/")
                    if file_id:
                        file_path = os.path.join(UPLOADS_DIR, f"{file_id}.txt")
                        try:
                            with open(file_path, "wb") as f:
                                f.write(flow.request.content)
                            ctx.log.info(f"📁 파일 저장: {file_path}")
                        except Exception as e:
                            ctx.log.error(f"파일 저장 실패: {e}")

    def response(self, flow: http.HTTPFlow):
        if flow.request.method != "POST":
            return
        content_type = flow.request.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            return

        try:
            body = json.loads(flow.request.get_text())
        except Exception as e:
            ctx.log.error(f"JSON parse error: {e}")
            return

        if "messages" not in body:
            return

        prompt_text = None
        attachments_info = []

        for message in body["messages"]:
            if message.get("author", {}).get("role") != "user":
                continue
            if message.get("content", {}).get("content_type") != "text":
                continue

            content_obj = message.get("content", {})
            if "parts" in content_obj:
                text_content = "\n".join(content_obj.get("parts", []))
            elif "text" in content_obj:
                text_content = content_obj.get("text")
            else:
                text_content = content_obj.get("content") or content_obj.get("value") or ""

            prompt_text = text_content.strip() if text_content else None
            if prompt_text:
                ctx.log.info(f"💬 프롬프트: {prompt_text}")

        for fname in os.listdir(UPLOADS_DIR):
            full_path = os.path.join(UPLOADS_DIR, fname)
            try:
                with open(full_path, "rb") as f:
                    file_bytes = f.read()
                mime_type = mimetypes.guess_type(fname)[0] or "application/octet-stream"
                extracted = self._extract_text(file_bytes, mime_type)

                # 올바른 테크스트 확인 및 바쁬 값 제거
                clean_extracted = [
                    line for line in extracted
                    if line and not line.strip().startswith("%PDF") and len(line.strip()) > 10 and '\x00' not in line
                ]

                if any(line.strip() for line in clean_extracted):
                    attachments_info.append({
                        "id": fname,
                        "name": fname,
                        "mime_type": mime_type,
                        "extracted_texts": clean_extracted
                    })
                    preview = "\n".join(clean_extracted)
                    ctx.log.info(f"📌 파일 테크스트 출존 ID={fname}, 이름={fname} \u21d2 \ucd9c존 \ud14c크스트: {preview}")
            except Exception as e:
                ctx.log.error(f"업로드 파일 분석 실패: {fname} - {e}")

        if prompt_text or attachments_info:
            event_obj = {
                "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "prompt": prompt_text,
                "attachments": attachments_info
            }
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filepath = os.path.join(SAVE_DIR, f"{timestamp}.json")
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(event_obj, f, ensure_ascii=False, indent=2)
                ctx.log.info(f"✅ 저장됨: {filepath}")
            except Exception as e:
                ctx.log.error(f"이벤트 저장 실패: {e}")

    def _extract_text(self, file_bytes, mime_type):
        try:
            if mime_type == "application/pdf":
                return self._extract_from_pdf(file_bytes)
            elif mime_type.startswith("image/"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                    tmp.write(file_bytes)
                    tmp_path = tmp.name
                text = pytesseract.image_to_string(Image.open(tmp_path))
                os.remove(tmp_path)
                return [text.strip()]
            else:
                detected = chardet.detect(file_bytes)
                encoding = detected.get("encoding") or "utf-8"
                ctx.log.info(f"🔍 인코딩 탐지: {encoding}")
                return [file_bytes.decode(encoding, errors="replace").strip()]
        except Exception as e:
            ctx.log.error(f"테크스트 추출 실패: {e}")
            return ["[텍스트 추출 실패]"]

    def _extract_from_pdf(self, file_bytes):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name
        texts = []
        try:
            with fitz.open(tmp_path) as doc:
                for page in doc:
                    texts.append(page.get_text().strip())
        except Exception as e:
            ctx.log.error(f"PDF 처리 실패: {e}")
        finally:
            os.remove(tmp_path)
        return texts

addons = [PromptLogger()]

