from flask import Blueprint, render_template
from werkzeug.utils import redirect
import FinanceDataReader as fdr
import pandas as pd
bp = Blueprint('stock', __name__, url_prefix='/')


# 이 stock_views.py 파일이 실제 FinanceDataReader에서 데이터를 가져오고 전처리 후 각 html파일로 데이터를 보내주는 역할을 할겁니다.
# 여기 코드가 길어질 가능성이 있기 때문에 추가로 function모듈을 만들고 그 모듈안에서 하나씩 함수를 호출해서 사용하는 방법이 좋을듯.


@bp.route('/kospi_nasdaq')
def ko_na(): # KOSPI & NASDAQ Category

    # 나스닥
    IXIC = fdr.DataReader('IXIC', '2016-01-04', '2021-12-31', data_source='close')

    IXIC.dropna(axis=0)

    # 코스피
    ks11 = fdr.DataReader('ks11', '2016-01-04', '2021-12-31', data_source='close')

    ks11.dropna(axis=0)

    stock_list = [
        ["NASDAQ", "IXIC"],
        ["KOSPI", "ks11"],
    ]

    df_list = [fdr.DataReader(code, '2016-01-04', '2021-12-31')['Close'] for name, code in stock_list]

    df = pd.concat(df_list, axis=1)
    df.columns = [name for name, code in stock_list]

    df.index = df.index.strftime('%Y/%m/%d')
    df = df.fillna(method='ffill')

    print(df)

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