from bs4 import BeautifulSoup
import requests

url = ['https://peopleparty.kr/press?sca=%EB%85%BC%ED%8F%89']

for i in range(2, 5):
    url.append(
        'https://peopleparty.kr/press?sca=%EB%85%BC%ED%8F%89&page=' + str(i))
finallist = []

for j in range(0, 4):
    req = requests.get(url[j])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.tit')

    for i in title:
        titleList = []
        titleList.append(i.a.text)
        titleList.append(i.a.attrs['href'])
        finallist.append(titleList)