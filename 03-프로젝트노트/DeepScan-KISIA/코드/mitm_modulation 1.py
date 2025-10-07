from mitmproxy import http, ctx

def request(flow: http.HTTPFlow) -> None:
    # 안전하게 헤더 조작 (기존 값을 덮어쓰지 않고, 없을 경우만 추가)
    flow.request.headers["User-Agent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/116.0.0.0 Safari/537.36"
    )
    flow.request.headers["Accept-Language"] = "en-US,en;q=0.9"

    # 로그 포맷 깔끔하게 출력
    ctx.log.info("=" * 60)
    ctx.log.info(f"📡 [Request] {flow.request.method} {flow.request.pretty_url}")
    ctx.log.info(f"📁 [Headers]\n{flow.request.headers}")

    if flow.request.content:
        try:
            content = flow.request.get_text()
            ctx.log.info(f"📝 [Body]\n{content}")
        except Exception as e:
            ctx.log.warn(f"⚠️ Failed to decode request body: {e}")

