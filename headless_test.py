from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=800x600')
#options.binary_location = '/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver',chrome_options=options)
