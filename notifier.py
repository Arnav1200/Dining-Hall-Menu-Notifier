import datetime as dt
import time
import smtplib
import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
while True:
    url = 'https://wlu.campusdish.com/en/LocationsAndMenus/FreshFoodCompany'
    ffc_r = requests.get(url)
    ffc_soup = BeautifulSoup(ffc_r.text, 'html.parser')
    all = ffc_soup.findAll('a', attrs={'class':'viewItem'})
    list_menu = ""
    for name in ffc_soup.findAll('a', attrs={'class':'viewItem'}):
        list_menu = list_menu + str(name.text) + ", "
    email_user = "*EMAIL GOES HERE*"
    server = smtplib.SMTP ("smtp.gmail.com", 587) 
    server.ehlo()
    server.starttls()
    server.login('#EMAILGOES HERE#', '#PASSWORD GOES HERE')
    message = normalize('NFKD', list_menu).encode('ASCII', 'ignore')
    server.sendmail(email_user, email_user, message)
    server.quit()
    time.sleep(60*360)
   

