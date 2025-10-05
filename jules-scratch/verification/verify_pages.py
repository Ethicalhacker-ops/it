import os
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')

        # Pages to verify
        pages = [
            "index.html",
            "about.html",
            "service.html",
            "contact.html",
            "blog.html",
            "detail.html",
            "feature.html",
            "price.html",
            "quote.html",
            "team.html",
            "testimonial.html"
        ]

        for page_name in pages:
            file_path = f"file://{os.path.join(base_path, page_name)}"
            page.goto(file_path)
            page.wait_for_load_state('networkidle')
            screenshot_path = f"jules-scratch/verification/{page_name.replace('.html', '.png')}"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()