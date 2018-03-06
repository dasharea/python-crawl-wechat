import urllib.request
import re
url="http://mp.weixin.qq.com/s?src=11&timestamp=1518149148&ver=687&signature=z8mFfnAr5biloNuvJ35L2MJo4DxhobOoL0CvyjlUUwEjjAGaI3VFUvRfHaishj3PkbeYrZqYrqyBDIprBvXYI*mMjFi9Cs5750O7xaB5FZ4aQGLEPcWsRSy6q6cXJt7q&new=1"
data=urllib.request.urlopen(url).read().decode("utf-8")
print (data)
titlepat='id="js_content">([\s\S]*?)id="js_sg_bar"'
title=re.compile(titlepat).findall(data,re.S)
print(title)
