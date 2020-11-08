#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import urllib.parse as parse
import urllib.request as req
import urllib

if len(sys.argv)<=1:
    print("python3 forecase.py 지역번호")
    sys.exit()
regionNumber = sys.argv[1]
API = "http://kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#서울 경기 지역 선택
values = {
    'stdId': str(regionNumber)
}
params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)
data = urllib.request.urlopen(url).read()
#바이너리 데이터를 문자열로 반환
text = data.decode("utf-8")
print(text)

