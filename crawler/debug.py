import urllib.request 

httpHandle = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandle)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com").read().decode('utf-8')
# print(len(data))
