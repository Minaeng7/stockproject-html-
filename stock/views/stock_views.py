import matplotlib.pyplot as plt
import pandas as pd
from flask import Blueprint, render_template, send_file
from werkzeug.utils import redirect
from stock.modules import kospi_nasdaq as kn
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
plt.style.use('ggplot')

bp = Blueprint('stock', __name__, url_prefix='/')


# 이 stock_views.py 파일이 실제 FinanceDataReader에서 데이터를 가져오고 전처리 후 각 html파일로 데이터를 보내주는 역할을 할겁니다.
# 여기 코드가 길어질 가능성이 있기 때문에 추가로 function모듈을 만들고 그 모듈안에서 하나씩 함수를 호출해서 사용하는 방법이 좋을듯.


@bp.route('/kospi_nasdaq')
def ko_na(): # KOSPI & NASDAQ Category

    # df = kn.kospiandnasdaq()
    df = pd.read_csv("C:\ACORN\stockproject-html-\stock\modules\kospi_nasdaq.csv", index_col=0)
    print(df)

    # fig, ax = plt.subplots()
    # date = df.columns
    # kospi = df["KOSPI"]
    # nasdaq = df["NASDAQ"]
    # plt.plot(date, kospi, color="blue")
    # plt.plot(date, nasdaq, color="red")
    # plt.xlabel('Date')
    # plt.ylabel('Kospi&Nasdaq')
    # plt.title('')
    # canvas = FigureCanvas(fig)
    # img = BytesIO()
    # fig.savefig(img)
    # img.seek(0)


    # return render_template('kospi_nasdaq.html'), send_file(img, mimetype='image/png')
    return render_template('kospi_nasdaq.html', df=df)


@bp.route('/stocks')
def stocks(): # STOCK OF KOSPI Category
    return render_template('stocks.html')


@bp.route('/stocks_nasdaq')
def st_na(): # STOCK & NASDAQ Category
    return render_template('stocks_nasdaq.html')


@bp.route('/coupling')
def couple(): # WHAT IS THE COUPLING Category
    return render_template('coupling.html')