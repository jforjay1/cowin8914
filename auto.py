from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
captchaarray = []
print("start")
driver = webdriver.Chrome(r"C:\Users\jaypa\Downloads\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get('https://web.umang.gov.in/web_new/login?redirect_to=department%3Furl%3Dcowin%2F%26dept_id%3D355%26dept_name%3DCo-WIN')
time.sleep(7)
driver.find_element_by_id('mat-input-0').send_keys('9712289689')

driver.find_element_by_id('mat-input-1').send_keys('8970')

driver.find_element_by_xpath("//*[@src='assets/img/refresh.svg']").click()
time.sleep(3)
contacts = driver.find_elements_by_css_selector('.captcha-letters span')
for contact in contacts:
    cap = contact.text
    captchaarray.append(cap)
listToStr = ''.join([str(elem) for elem in captchaarray])
driver.find_element_by_id('mat-input-2').send_keys(listToStr)
driver.find_element_by_class_name('btn').send_keys(Keys.ENTER)
time.sleep(20)
im = driver.find_element_by_xpath('/html/body/app-root/app-app-root/app-app-home/div/div[1]/ul/li[1]/app-app-tile/div/a[2]/img').click()
im[0].send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name('apt-btn link-primary schedule ng-star-inserted').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name('mat-focus-indicator mat-menu-item').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_id('mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored ng-dirty ng-valid ng-touched').send_keys('388150')
time.sleep(2)
driver.find_element_by_class_name('btn').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name('btn mat-button mat-button-base').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_class_name('chips success ng-star-inserted').send_keys(Keys.ENTER)
time.sleep(2)
#driver.find_element_by_class_name('slot-chips').send_keys(Keys.ENTER)
slots = driver.find_elements_by_css_selector('.captcha-letters span')
for slot in slots:
    print(slot.text)

time.sleep(20)
#driver.find_element_by_class_name('user-menu action-btn-header mat-focus-indicator mat-menu-trigger mat-ripple mat-button mat-button-base').send_keys(Keys.ENTER)
#driver.find_element_by_class_name('mat-focus-indicator mat-menu-item').send_keys(Keys.ENTER)
driver.close()
print('end')