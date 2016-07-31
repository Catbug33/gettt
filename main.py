# coding=utf-8

import time

from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get("http://booking.uz.gov.ua")
print driver.title
driver.find_element_by_name('station_from').send_keys('Zaporizhzhya 1')
time.sleep(2)
driver.find_element_by_xpath("//div[@title='Zaporizhzhya 1']").click()
driver.find_element_by_name('station_till').send_keys('Kyiv')
time.sleep(2)
driver.find_element_by_xpath("//div[@title='Kyiv']").click()
driver.find_element_by_name('date_dep').click()
driver.find_element_by_xpath('//td[@data-month="7" and @data-year="2016"]/a[contains(., "10")]').click()
driver.find_element_by_name('search').click()
time.sleep(5)
routes_available_locator = '//table[@id="ts_res_tbl"]/tbody/tr'
routes_available = len(driver.find_elements_by_xpath(routes_available_locator))
print routes_available
for i in xrange(routes_available):
    wagen_klass_locator_iter = routes_available_locator + '[{0}]'.format(i + 1)
    wagen_klass_locator = wagen_klass_locator_iter + '/td[@class="place"]/div'
    train_num = driver.find_element_by_xpath(wagen_klass_locator_iter + '/td[@class="num"]/a').get_attribute('innerHTML')
    # Train num
    print train_num
    wagen_klass_number = len(driver.find_elements_by_xpath(wagen_klass_locator_iter + '/td[@class="place"]/div'))
    print wagen_klass_number
    for j in xrange(wagen_klass_number):
        print driver.find_element_by_xpath(wagen_klass_locator + '[' + str(j + 1) + ']').get_attribute('title'), ':', \
            driver.find_element_by_xpath(wagen_klass_locator + '[' + str(j + 1) + ']/b').get_attribute('innerHTML')

driver.save_screenshot('1.png')

driver.close()
