import json
import plotly.utils
import matplotlib
matplotlib.use('Agg')
import pandas as pd
from flask import Blueprint, render_template, send_file, make_response, url_for, Response
from stock.modules import kospi_nasdaq as kn
import plotly
import plotly.graph_objs as go

bp = Blueprint('stock', __name__, url_prefix='/')

# kospi_nasdaq
df = kn.kospiandnasdaq()

@bp.route('/kospi_nasdaq')
def ko_na(): # KOSPI & NASDAQ Category

    # 코스피, 나스닥 그래프
    bar = knplot()
    return render_template('kospi_nasdaq.html', plot=bar)

# 그래프
def knplot():

    data = [
        go.Scatter(x=df.index, y=df["KOSPI"]),
        go.Scatter(x=df.index, y=df["NASDAQ"], yaxis='y2')
    ]

    y2 = go.YAxis(overlaying='y', side='right')
    layout = go.Layout(yaxis2=y2)
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(go.Layout(paper_bgcolor='#30254D',
                                legend={'font':{'color':'#000000'}},
                                font={'color':'white'}))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@bp.route('/stocks')
def stocks(): # STOCK OF KOSPI Category
    return render_template('stocks.html')


@bp.route('/stocks_nasdaq')
def st_na(): # STOCK & NASDAQ Category
    return render_template('stocks_nasdaq.html')


@bp.route('/coupling')
def couple(): # WHAT IS THE COUPLING Category
    return render_template('coupling.html')