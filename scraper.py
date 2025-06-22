from playwright.sync_api import sync_playwright

def fetch_content_with_header(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(url, wait_until='load', timeout=45000)

        except Exception as e:
            return "Unknown Page", f"Navigation timeout or blocked: {e}"

        title = page.title()

        # Try common article wrappers
        candidates = [
            "article", "main", "div#content", "div.post", 
            "div.entry-content", "section", "div[class*=content]"
        ]

        content = ""
        for selector in candidates:
            if page.locator(selector).count() > 0:
                text = page.locator(selector).first.inner_text()
                if len(text.split()) > 100:
                    content = text
                    break

        if not content:
            content = "Could not extract meaningful content."

        browser.close()
        return title, content
