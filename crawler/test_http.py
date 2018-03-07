import urllib.request

response = urllib.request.urlopen(
    "http://blog.csdn.net/weiwei_pig/article/details/51178226")
html = response.read()
print(response.info())
print(response.geturl())

# savefile = open('../1.html','wb')
# savefile.write(html)
# savefile.close()

# urllib.request.urlretrieve("http://www.baidu.com","../2.html")
