from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    def handle_response(response):
        if hasattr(response, 'url') and ('amazon.com' in response.url or 'amazonaws' in response.url):
            if 'html' not in response.url and 'js' not in response.url and 'css' not in response.url:
                try:
                    if 'application/json' in response.headers.get('content-type', ''):
                        data = response.json()
                        node_count = 0
                        if 'data' in data:
                            node_count = len(data['data'])
                        elif 'Node' in data:
                            node_count = 1
                        if node_count > 0:
                            print(f"[FOUND] {response.url} - Has {node_count} items")
                            print(str(data)[:200])
                except:
                    pass

    page.on("response", handle_response)
    print("Navigating to URL...")
    page.goto("https://www.amazon.com/photos/shared/c0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB", wait_until="networkidle", timeout=30000)
    
    # wait an additional 5 seconds for React to fetch everything
    time.sleep(5)
    print("Done waiting.")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
