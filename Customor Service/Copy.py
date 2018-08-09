from selenium import webdriver
from tkinter import Tk

#sign in
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver')
driver.get('https://r2games.desk.com/login/new')
account = driver.find_element_by_name('user_session[email]')
password = driver.find_element_by_name('user_session[password]')
login = driver.find_elements_by_id('user_session_submit')
account.send_keys('sheldon@r2games.com')
password.send_keys('Yyyy6666')
account.submit()

def copy():
    tk = Tk()
    tk.withdraw()
    tk.clipboard_clear()
    server_name = driver.find_element_by_xpath('//*[@id="ticket_custom1"]')
    char_name = driver.find_element_by_xpath('//*[@id="ticket_custom4"]')
    account = driver.find_element_by_xpath('//*[@id="ticket_custom6"]')
    user_id = driver.find_element_by_xpath('//*[@id="ticket_custom7"]')
    return server_name.value
    
    
    
