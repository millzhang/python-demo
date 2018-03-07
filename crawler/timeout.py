import urllib.request

url = "http://github.com"

for i in range(1,100):
    try:
        data = urllib.request.urlopen(url,timeout=1).read()
        print(data)
    except Exception as e:
        print("Exception==>"+str(e))
    

