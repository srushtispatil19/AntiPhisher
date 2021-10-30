##import webbrowser
##
##new = 2
##url = "http://whois.domaintools.com/"
##term = input("Enter domain name: ");
##
##webbrowser.open(url+term,new=new)

import requests

def main():
    query = input("Enter domain name: ")
    search = "http://whois.domaintools.com/"+query
    r = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
    print (r.text)
## https://verif-account.myvnc.com/
##def main():
##    query = input("Enter url: ")
##    search = "view-source:"+query
##    r = requests.get(search, headers={"User-Agent": "Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/53.0.2785.143 Safari/537.36"})
##    print (r.text)

if __name__ == '__main__':
    main()
