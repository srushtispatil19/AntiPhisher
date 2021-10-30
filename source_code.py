import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import requests
import sys
##code = []
##response = urllib.request.urlopen("https://whois.icann.org/en/lookup?name=google")
##page_source = response.read()
##code = page_source
##print(code)



####query = input("Enter domain name: ")


search = "https://www.whois.com/whois/google.com"
thepage = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup3 = BeautifulSoup(thepage.content, "html.parser")


#print(soup3.prettify())
a = soup3.find_all("pre", class_="df-raw")[0].get_text()
#
#for a in soup3.findAll('div', {"class":"contact-info-wrappers"}):
####
print(a)

##data = requests.get('https://www.whois.com/whois/google.com')
##dom = re.findall(r'(Domain:)',data.text)
##print(dom)







######################################   Feature 10 =======  Abnormal URL   ###############


##search = "https://www.whois.com/whois/"+domain_name
##thepage = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
##soup3 = BeautifulSoup(thepage.content, "html.parser")
##
##a = soup3.find_all("div", class_="df-value")[0].get_text()
##if(a==domain_name):
##    test_sample.append(-1)
##else:
##    test_sample.append(1)
