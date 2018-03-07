import re  #导入正则模块
import urllib.request


def claw(url, page):
    html = urllib.request.urlopen(url).read()
    htmlStr = str(html)
    petternStr = '<img width="220" height="220" class="err-product" data-img="1" data-lazy-img="//(.+?\.jpg)" />'
    image_list = re.compile(petternStr).findall(htmlStr)
    index = 1
    for item in image_list:
        try:
            imageUrl = "http://" + item
            urllib.request.urlretrieve(
                imageUrl,
                "G:/github/clawler/" + str(page) + "-" + str(index) + ".jpg")
        except Exception as e:
            print("出现异常=>" + str(e))
            index += 1
        index += 1
    print('爬行数量=>'+str(len(image_list)))


def run():
    rootUrl = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page="
    for i in range(1, 100):
        claw(rootUrl + str(i), i)


run()