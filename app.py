# app.py
from flask import Flask, render_template
import theminjoo_briefing as mjb
import theminjoo_report as mjr
import peoplepower as pow
import justice as jus
import peopleparty_briefing as peob
import peopleparty_report as peor
import article as art

# Flask 객체 인스턴스 생성
app = Flask(__name__)


@app.route('/')  # 접속하는 url
def index():
    return render_template('index.html')


@app.route('/party1')
def party1():
    return render_template('party1.html')


@app.route('/party1/party1-1')
def party1_1():
    return render_template('party1-1.html', list=mjb.finallist)


@app.route('/party1/party1-2')
def party1_2():
    return render_template('party1-2.html', list=mjr.finallist)

@app.route('/party2')
def party2():
    return render_template('party2.html')


@app.route('/party2/party2-1')
def party2_1():
    return render_template('party2-1.html', list=pow.briefinglist)


@app.route('/party2/party2-2')
def party2_2():
    return render_template('party2-2.html', list=pow.reportlist)


@app.route('/party3')
def party3():
    return render_template('party3.html')


@app.route('/party3/party3-1')
def party3_1():
    return render_template('party3-1.html', list=jus.briefinglist)


@app.route('/party3/party3-2')
def party3_2():
    return render_template('party3-2.html', list=jus.reportlist)

@app.route('/party4')
def party4():
    return render_template('party4.html')

@app.route('/party4/party4-1')
def party4_1():
    return render_template('party4-1.html', list=peob.finallist)


@app.route('/party4/party4-2')
def party4_2():
    return render_template('party4-2.html', list=peor.finallist)

@app.route('/agendamain')
def agendamain():
    return render_template('agendamain.html')

@app.route('/buildings')
def buildings():
    return render_template('buildings.html',
                            list1 = art.powerB, list2 = art.minB, list3 = art.jusB, list4 = art.peoB)
@app.route('/economy')
def economy():
    return render_template('economy.html',
                            list1=art.powerE, list2=art.minE, list3=art.jusE, list4=art.peoE)
@app.route('/finance')
def finance():
    return render_template('finance.html',
                           list1=art.powerF, list2=art.minF, list3=art.jusF, list4=art.peoF)
@app.route('/wellbeing')
def wellbeing():
    return render_template('wellbeing.html',
                           list1=art.powerW, list2=art.minW, list3=art.jusW, list4=art.peoW)

if __name__ == "__main__":
    app.run(debug=True)
