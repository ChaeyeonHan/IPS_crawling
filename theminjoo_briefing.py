from bs4 import BeautifulSoup
import requests

url = ['https://theminjoo.kr/board/lists/briefing']

for i in range(2, 5):
    url.append('https://theminjoo.kr/board/lists/briefing?page=' + str(i))
finallist = []

for j in range(0, 4):
    req = requests.get(url[j])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.subject.clearfix')

    for i in title:
        titlelist = []
        titlelist.append(i.a.text)
        titlelist.append('https://theminjoo.kr/' + i.a.attrs['href'])
        finallist.append(titlelist)