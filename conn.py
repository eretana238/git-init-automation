from selenium import webdriver
import time

def browse(username, password, project_name):
    url = 'https://www.github.com/login'
    browser = webdriver.Chrome()
    browser.get(url)
    # inserts user info at login
    login_user = browser.find_element_by_id('login_field')
    login_user.clear()
    login_user.send_keys(username)
    pass_user = browser.find_element_by_id('password')
    pass_user.clear()
    pass_user.send_keys(password)
    button = browser.find_element_by_name('commit')
    button.click()
    return create_repo(browser, project_name)

def create_repo(browser, project_name):
    browser.get('https://github.com/new')
    # inserts project name
    name = browser.find_element_by_id('repository_name')
    name.send_keys(project_name)
    time.sleep(2)
    button = browser.find_element_by_css_selector('button.first-in-line')
    button.submit()
    # copy remote repository link
    link = browser.find_element_by_xpath('//*[@id="empty-setup-clone-url"]')
    return link.get_attribute('value')

