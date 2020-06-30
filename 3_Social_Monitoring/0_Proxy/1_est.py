import urllib.request  as urllib2

#proxy = urllib2.ProxyHandler({"http": "192.168.0.255:8888"})
#proxy = urllib2.ProxyHandler({"http": "118.69.140.108:53281"})
proxy = urllib2.ProxyHandler({"http": "64.227.106.79:8080"})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
print("----")
page = urllib2.urlopen("http://www.python.org/").read(100)
print(page)

