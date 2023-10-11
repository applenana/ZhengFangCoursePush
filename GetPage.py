LoginSite=''
CourseSite=''
Account=''
SecretKey=''

from playwright.sync_api import Playwright, sync_playwright, expect
def GetPagef():
    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(LoginSite)
        page.get_by_placeholder("用户名").click()
        page.get_by_placeholder("用户名").fill(Account)
        page.get_by_placeholder("密码").click()
        page.get_by_placeholder("密码").fill(SecretKey)
        page.get_by_placeholder("密码").press("Enter")
        page.wait_for_load_state('networkidle')
        page.goto(CourseSite)
        page.wait_for_timeout(100)
        while not page.locator('text="的课表"').first.is_visible():
            page.wait_for_timeout(100)
            print('wating data......')
        content=page.content()
        # ---------------------
        context.close()
        browser.close()
        with open('test.html','w',encoding='utf-8') as f:
            f.write(str(content))
        return(content)

    with sync_playwright() as playwright:
        return(run(playwright))
    
#print(GetPage())

