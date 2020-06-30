import fileinput # accept proxies from files or stdin

try:
    print("-- Gevent Pool ")
    from gevent.pool import Pool # $ pip install gevent
    import gevent.monkey; gevent.monkey.patch_all() # patch stdlib
except ImportError: # fallback on using threads
    #print("-- Failed")
    from multiprocessing.dummy import Pool

try:
    print("-- URLLIB")
    from urllib2 import ProxyHandler, build_opener
except ImportError: # Python 3
    #print("-- Failed")
    from urllib.request import ProxyHandler, build_opener

def is_proxy_alive(proxy, timeout=5):
    opener = build_opener(ProxyHandler({'http': proxy})) # test redir. and such
    try: # send request, read response headers, close connection
        opener.open("http://www.google.com", timeout=timeout).close()
    except EnvironmentError:
        return None
    else:
        return proxy

candidate_proxies = (line.strip() for line in fileinput.input())
pool = Pool(5) # use 20 concurrent connections
print("-- Past POOL")

for proxy in pool.imap_unordered(is_proxy_alive, candidate_proxies):
    print("--")
    print(proxy)
    if proxy is not None:
       print("-")
       print(proxy)



# python alive-proxies.py proxy.txt
# echo user:password@ip:port | python alive-proxies.py
