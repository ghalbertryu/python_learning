from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# firefox plugin
# https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu

# hide browser window
chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless


# add the option when creating driver
driver = webdriver.Chrome('D:\PyWork\chromedriver', options=chrome_options) #options=chrome_options
###################################
driver.get("https://morvanzhou.github.io/about/")
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='大家说'])[1]/preceding::strong[1]").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"Python基础 ▾").click()
driver.find_element_by_link_text(u"多进程 multiprocessing").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"提效工具 ▾").click()
driver.find_element_by_link_text(u"Git 版本管理").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='大家说'])[1]/preceding::strong[1]").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"Python基础 ▾").click()
driver.find_element_by_link_text(u"多进程 multiprocessing").click()

###################################
print(driver.page_source[:200])
driver.get_screenshot_as_file(".\\img\\sreenshot1.png")
driver.close()
print('finish')