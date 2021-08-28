from bs4 import BeautifulSoup
import requests

url = 'http://www.peoplepowerparty.kr/renewal/news/briefing_delegate.do'

briefinglist = []
reportlist = []

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select('td.subject')

for i in title:
    titlelist = []
    titlelist.append(i.a.text)
    onClick = i.a.attrs['onclick']
    plusUrl = onClick[onClick.find('(')+2:onClick.find(')')-1]
    titlelist.append(
        'http://www.peoplepowerparty.kr/renewal/news/briefing_delegate_view.do?bbsId=' + plusUrl)

    if titlelist[0].find('보도자료') != -1:
        reportlist.append(titlelist)
    elif titlelist[0].find('논평') != -1:
        briefinglist.append(titlelist)