from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        log = "Jarmil"
        pasw = "Admin123"

        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill("input['id =login']", log)
        page.fill("input['id =login']", pasw)

        page.click("button['class=login-btn']")
        page.wait_for_timeout(1000)

        secr = page.get_by_placeholder("psst").text_content()
        print(secr)

        input("Klikni na cokoliv pro zavření prohlížeče")
        browser.close()
    

if __name__ == "__main__":
    main()
