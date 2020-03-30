from selenium import webdriver
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
