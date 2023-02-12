import requests

domain = input("enter domain => ")
list = open(input("enter list => "),"r")
subdomains = list.read().splitlines()

for subdomain in subdomains:
    http = ("http://%s.%s"%(subdomain,domain))
    https = ("https://%s.%s"%(subdomain,domain))
    try:
        requests.get(http)
        print(http)
    except requests.ConnectionError:
        pass
    try:
        requests.get(https)
        print(https)
    except requests.ConnectionError:
        pass

