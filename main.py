import requests
from bs4 import BeautifulSoup
import pprint
import smtplib

my_email = "neryamanassentest@gmail.com"
password = "password"



def fix_string(str):
    length = len(str)-1
    str = list(str)
    for i in range(0,length):
        str[i]=str[i+1]
    get_rid_of_last_two_elements(str,length)
    return str
def get_rid_of_last_two_elements(str,length):
    str[length] = ''
    str[length-1] = ''
    return str

def check_price(price):
    if price < 20:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="neryamanassen9@gmail.com",
                                msg="Subject:Hello\n\n")
    return "mail have been sent"



headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
"Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7"
}
url = "https://www.amazon.com/-/he/dp/B07BX99JZ4/ref=bmx_dp_3/146-2487696-8153602?pd_rd_w=KEzz6&pf_rd_p=b7fa5431-ff87-43ac-9073-fcdf928ec25c&pf_rd_r=XWA1KCBV2K5WHVT3ZHTH&pd_rd_r=38d928c5-ae17-4ab3-8ef8-481202f7d266&pd_rd_wg=ka5qT&pd_rd_i=B07BX99JZ4&psc=1"
response = requests.get(url=url,headers = headers)

html_doc = response.text
print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')

price = soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()
price_without_currency = price.split("$")[0]
string = fix_string(price_without_currency)
price_without_currency = float("".join(string))
check_price(price_without_currency)
