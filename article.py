from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests

baseUrl = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='

urlList = []
powerE = []  # 국힘 경제
powerB = []  # 국힘 부동산
powerW = []  # 국힘 복지
powerF = []  # 국힘 재정
minE = []  # 더민 경제
minB = []  # 더민 부동산
minW = []  # 더민 복지
minF = []  # 더민 재정
jusE = []  # 정의 경제
jusB = []  # 정의 부동산
jusW = []  # 정의 복지
jusF = []  # 정의 재정
peoE = []  # 국민 경제
peoB = []  # 국민 부동산
peoW = []  # 국민 복지
peoF = []  # 국민 재정
nameList = ['국민의힘', '더불어민주당', '정의당', '국민의당']
agendaList = ['경제', '부동산', '복지', '재정']

for i in nameList:
    for j in agendaList:
        plusUrl = i + ' ' + j
        url = baseUrl + quote_plus(plusUrl)
        urlList.append(url)



for i in range(0, len(nameList)*len(agendaList)):
    req = requests.get(urlList[i])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.news_tit')

    titleList = []
    for j in title:
        titleList = []
        titleList.append(j.text)
        titleList.append(j.attrs['href'])

        if i == 0:
            powerE.append(titleList)
        elif i == 1:
            powerB.append(titleList)
        elif i == 2:
            powerW.append(titleList)
        elif i == 3:
            powerF.append(titleList)

        elif i == 4:
            minE.append(titleList)
        elif i == 5:
            minB.append(titleList)
        elif i == 6:
            minW.append(titleList)
        elif i == 7:
            minF.append(titleList)

        elif i == 8:
            jusE.append(titleList)
        elif i == 9:
            jusB.append(titleList)
        elif i == 10:
            jusW.append(titleList)
        elif i == 11:
            jusF.append(titleList)

        elif i == 12:
            peoE.append(titleList)
        elif i == 13:
            peoB.append(titleList)
        elif i == 14:
            peoW.append(titleList)
        elif i == 15:
            peoF.append(titleList)