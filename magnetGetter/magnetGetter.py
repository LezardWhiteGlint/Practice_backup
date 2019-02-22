from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver')
result = []
page = 1
maxPage = 13
partialUrl = "https://sukebei.nyaa.si/?f=0&c=1_5&q=%E6%AF%8D&p="
def getLinks(url = partialUrl,page = page, maxPage = maxPage):
    while page <= maxPage:
        driver.get(url+str(page))
        row = 1
        while True:
            try:
                link = driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr["+str(row)+"]/td[3]/a[2]")
                result.append(link.get_attribute("href"))
                row += 1
            except NoSuchElementException:
                page += 1
                break

    f = open("out.txt", "w")
    for r in result:
        f.write(r)
        f.write("\n")
    f.close()
    driver.quit()

getLinks()
