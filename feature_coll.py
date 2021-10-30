import numpy
import re
import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import sys
from datetime import datetime
import datetime
from numpy import array
##str = "The rain in Spain"
##x = re.split("\s", str, 1)
##print(x[1])
test_sample = []

url = 'https://serviswer-prestion.co.uk/swc/'

################ Feature 1 ===== IP address##########
start = '//'
end = '/'
domain_name = ((url.split(start))[1].split(end)[0])
print (domain_name)

digits = re.findall("\d", domain_name)
if (digits):
    test_sample.append(1)
else:
    test_sample.append(-1)

#########  Feature 2 ===== URL length ##############

url_len = len(url)
if (url_len>200):
    test_sample.append(1)
else:
    test_sample.append(0)


############# Feature 3 ===== subdomain #####################

count = 0
  
for i in domain_name: 
    if i == '.': 
        count = count + 1
#print(count)
if (count>3):
    test_sample.append(1)
elif (count==3):
    test_sample.append(0)
else:
    test_sample.append(-1)


################# Feature 4 ===== domain length  ################

if ((len(domain_name))>45):
    test_sample.append(1)
else:
    test_sample.append(-1)


################### Feature 5 ======== //   ###############

slash = re.findall("//", url)
count1 = len(slash)
##print(count1)
if (count1>1):
    test_sample.append(1)
else:
    test_sample.append(-1)

##print (test_sample)

################# Feature 6 ========= HTTPS  #######################

https = re.search("^https", url)
if(https):
    test_sample.append(-1)
else:
    test_sample.append(1)


##################### Feature 7 ====== Request URLs ##################

same_domain1=0
diff_domain1=0
number_of_req=0
percent_same1=0
percent_diff1=0
#theurl = 'https://stackoverflow.com/questions/3368969/find-string-between-two-substrings'
thepage = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup1 = BeautifulSoup(thepage.content, "html.parser")
fi = open('req_url.txt',"w")
for req in soup1.findAll('img', attrs={'src': re.compile("^https://")}):
    fi.write(req.get('src'))
    fi.write("\n")
    number_of_req = number_of_req + 1

fi = open('req_url.txt',"a")

for req1 in soup1.findAll('img', attrs={'src': re.compile("^http://")}):
    ##print(link1.get('href')
    fi.write(req1.get('src'))
    fi.write("\n")
    number_of_req = number_of_req +1

    
fi = open('req_url.txt',"a")

for req2 in soup1.findAll('script', attrs={'src': re.compile("^https://")}):
    #print("Script tag: ",req2.get('src'))
    fi.write(req2.get('src'))
    fi.write("\n")
    number_of_req = number_of_req +1

fi = open('req_url.txt',"a")

for req3 in soup1.findAll('script', attrs={'src': re.compile("^http://")}):
    ##print(link1.get('href')
    fi.write(req3.get('src'))
    fi.write("\n")
    number_of_req = number_of_req +1

fi.close()
#print("number_of_req= ",number_of_req)

fil = open('req_url.txt',"r")   
for ri in fil:
    dom_name = ((ri.split(start))[1].split(end)[0])
    #print(dom_name)
    #print(same_domain1,diff_domain1)
    if(dom_name==domain_name):
        same_domain1 = same_domain1+1
    else:
        diff_domain1 = diff_domain1+1



percent_same1 = (same_domain1/number_of_req)*100
percent_diff1 = (diff_domain1/number_of_req)*100
#print(percent_same1,percent_diff1)

if(percent_same1<20):
    test_sample.append(1)
elif(percent_same1>20 and percent_same1<50):
    test_sample.append(0)
else:
    test_sample.append(-1)



######################### Feature 8 ======== URL of <a>  ###############
same_domain=0
diff_domain=0
number_of_url=0
percent_same=0
percent_diff=0

#theurl = 'https://stackoverflow.com/questions/3368969/find-string-between-two-substrings'
thepage = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup = BeautifulSoup(thepage.content, "html.parser")
file = open('url_a.txt',"w")
for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    file.write(link.get('href'))
    file.write("\n")
    number_of_url = number_of_url + 1
file = open('url_a.txt',"a")

for link1 in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    ##print(link1.get('href')
    file.write(link1.get('href'))
    file.write("\n")
    number_of_url = number_of_url +1
file.close()

f = open('url_a.txt',"r")   
for u in f:
    domain_name1 = ((u.split(start))[1].split(end)[0])
    if(domain_name1==domain_name):
        same_domain = same_domain+1
    else:
        diff_domain = diff_domain+1

percent_same = (same_domain/number_of_url)*100
percent_diff = (diff_domain/number_of_url)*100
#print(percent_same,percent_diff)

if(percent_same<20):
    test_sample.append(1)
elif(percent_same>20 and percent_same<50):
    test_sample.append(0)
else:
    test_sample.append(-1)



###############################  Feature 9 ============  <link> <meta> ################3
same_domain2=0
diff_domain2=0
number_of_link=0
percent_same2=0
percent_diff2=0

#theurl = 'https://stackoverflow.com/questions/3368969/find-string-between-two-substrings'
thepage = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup2 = BeautifulSoup(thepage.content, "html.parser")
fill = open('link_tag.txt',"w")
for li in soup2.findAll('link', attrs={'href': re.compile("^https://")}):
    #print(li.get('href'))
    fill.write(li.get('href'))
    fill.write("\n")
    number_of_link = number_of_link + 1

fill = open('link_tag.txt',"a")
for lin in soup2.findAll('link', attrs={'href': re.compile("^http://")}):
    fill.write(lin.get('href'))
    fill.write("\n")
    number_of_link = number_of_link + 1

fill = open('link_tag.txt',"a")
for lin1 in soup2.findAll('meta', attrs={'content': re.compile("^https://")}):
    #print(lin1.get('content'))
    fill.write(lin1.get('content'))
    fill.write("\n")
    number_of_link = number_of_link + 1

fill = open('link_tag.txt',"a")
for lin2 in soup2.findAll('meta', attrs={'content': re.compile("^http://")}):
    #print(lin2.get('content'))
    fill.write(lin2.get('content'))
    fill.write("\n")
    number_of_link = number_of_link + 1

c=0
fili = open('link_tag.txt',"r")   
for u2 in fili:
    c=c+1
    d_name = ((u2.split(start))[1].split(end)[0])
    if(d_name==domain_name):
        same_domain2 = same_domain2+1
    else:
        diff_domain2 = diff_domain2+1


fili.close()
#print(c,same_domain2,diff_domain2,number_of_link)   not considering last line in file

percent_same2 = (same_domain2/number_of_link)*100
percent_diff2 = (diff_domain2/number_of_link)*100

#print(percent_same2,percent_diff2)

if(percent_same2<20):
    test_sample.append(1)
elif(percent_same2>20 and percent_same2<50):
    test_sample.append(0)
else:
    test_sample.append(-1)



################################# Feature 10 ==== Abnormal URL  ###########

search = "https://www.whois.com/whois/"+url
thepage = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup3 = BeautifulSoup(thepage.content, "html.parser")


err = soup3.find('div', {"class":"whois_errorbox"})
if(err):
    test_sample.append(1)

else:
    
    ab = soup3.find_all("div", class_="df-value")[0].get_text()
    if(ab==domain_name):
        test_sample.append(-1)
    else:
        test_sample.append(1)


###############################################   Feature 11 =======  Pop up   ###############

test_sample.append(0)


###############################################   Feature 12 =======  Iframe   ###############

search = "https://www.whois.com/whois/"+url
thepage = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup3 = BeautifulSoup(thepage.content, "html.parser")
flag = 0
for a in soup3.findAll('iframe', {"frameborder":"0"}):
    flag = 1

if(flag==0):
    test_sample.append(-1)
else:
    test_sample.append(1)
    

#######################################  Feature 13 ======= age of domain ######################3
diff = 0
mon_diff = 0
yr_diff = 0
diff = 0
i = 1
#age = ""
##a1 = soup3.find_all("div", class_="df-value").get_text()
##print(a1)

err = soup3.find('div', {"class":"whois_errorbox"})
#err_msg = err.find('b')
if(err):
    test_sample.append(1)
 
else:
    
    value = []
    for a1 in soup3.find_all('div', {"class":"df-value"}):
        value.append(a1.get_text())
        

    for a2 in value:
        text1 = re.search("^(19|20)\d\d([- /.])", a2)
        if(text1):
            age = a2
            break

    print(age)
    #age = soup3.findAll("div", class_="df-value")[2].get_text()
    sys_date = datetime.datetime.now()
    curr_month = sys_date.month
    curr_year = sys_date.year
    dom_year = age[:4]
    dom_month = age[5:7]

    if(curr_year==dom_year):
        mon_diff = curr_month - int(dom_month)
        if(mon_diff >= 6):
            test_sample.append(-1)
        else:
            test_sample.append(1)

    elif(dom_year[:2] == '19'):
        age1 = int(dom_year[2:4])+1
        diff = 100-age1             ###### if year is 1997 ---> (2000-1998)
        yr_diff = diff + 18
        mon_diff = (12 - int(dom_month))+ (curr_month-1)
        age_in_months = (yr_diff*12)+mon_diff
        #print("Age of Domain: ", age_in_months)
        if(age_in_months >= 6):
            test_sample.append(-1)
        else:
            test_sample.append(1)
     
    elif(dom_year[:2] == '20'):
        age1 = int(dom_year[2:4])+1
        if(age1<18):
            yr_diff = 18 - int(age1)
        else:
            yr_diff = 0
        mon_diff = (12 - int(dom_month))+ (curr_month-1)
        age_in_months = (yr_diff*12)+mon_diff
        if(age_in_months >= 6):
            test_sample.append(-1)
        else:
            test_sample.append(1)

#print now.year, now.month, now.day, now.hour, now.minute, now.second



######################### Feature 14 ====== DNS record ##################

search1 = "https://www.whois.com/whois/"+url
thepage = requests.get(search1, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup4 = BeautifulSoup(thepage.content, "html.parser")


error = soup4.find('div', {"class":"whois_errorbox"})
#error_msg = error.find('b')

if(error):
    test_sample.append(1)
else:
    test_sample.append(-1)
    


##################################3 Feature 15 ========= Redirect #############3






########################## Feature 16 ====== website traffic ###############

pg_rank = "https://www.alexa.com/siteinfo/"+url
thepage = requests.get(pg_rank, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
soup5 = BeautifulSoup(thepage.content, "html.parser")

rank = soup5.find('strong', {"class":"metrics-data align-vmiddle"})

page_rank = rank.find('span')

print(page_rank.get_text())

if((page_rank.get_text()) == "-"):
    test_sample.append(1)

else:
    
    if(int(page_rank) <= 1000000):
        test_sample.append(-1)
    else:
        test_sample.append(1)
    
print (test_sample)

x = array([test_sample])
print(x)



