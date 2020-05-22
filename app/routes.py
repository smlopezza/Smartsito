from flask import render_template, flash, redirect, url_for, request
from app import app

from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse
import plotly
#import plotly.graph_objs as go
import plotly.express as px

import json

import pandas as pd


x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']#np.linspace(0, 1, N)
units = [1530, 5117, 9779, 9187, 13817, 10769, 5761, 15210, 9050, 19720, 17200, 20700] #np.random.randn(N)
df = pd.DataFrame({'x': x, 'units': units}) # creating a sample dataframe
df['earnings'] = 3*df['units']

stores = ['Costco', 'Freshco', 'Metro', 'Food Basics', 'Shopers', 'Walmart']
FoodWasted = ['47%', '30%', '52%', '37%', '43%', '32%']
Consumers = [200, 400, 672, 987, 87, 176]
df_stores = pd.DataFrame({'Store': stores, 'Food Wasted': FoodWasted, 'Consumers': Consumers})

HotProducts_name = ['Milk', 'Eggs', 'Yogurt', 'Almond Milk', 'Cheese', 'Ice Cream', 'Sour Cream']
HotProducts_units = [470, 3000, 5290, 370, 413, 3221, 322]
HotProducts_earnings = [2210, 4050, 6720, 987, 1817, 1769, 1761]
df_HotProducts = pd.DataFrame({'Product':HotProducts_name, 'Units': HotProducts_units, 'Earnings': HotProducts_earnings })


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/ConsumerView')
def ConsumerView():
    return render_template('ConsumerView.html', user = 1)

@app.route('/RetailerView')
def RetailerView():
    figure01 = create_plot()
    return render_template('RetailerView.html', user = 2, plot=figure01)

@app.route('/ConsumerSavings')
def ConsumerSavings():
    return render_template('ConsumerSavings.html', user = 1)

@app.route('/ConsumerProducts')
def ConsumerProducts():
    return render_template('ConsumerProducts.html', user = 1)

@app.route('/ConsumerRewards')
def ConsumerRewards():
    return render_template('ConsumerRewards.html', user = 1)

@app.route('/RetailerHotProducts')
def RetailerHotProducts():
    figure03 = create_pieProducts()
    figure04 = create_plotProducts()
    return render_template('RetailerHotProducts.html', user = 2 ,  plot01=figure03, plot02=figure04, df_HotProducts = df_HotProducts)

@app.route('/RetailerPredictions')
def RetailerPredictions():
    figure01 = create_plot()
    return render_template('RetailerPredictions.html', user = 2, plot=figure01, dfPredicitons = df )

@app.route('/RetailerStore')
def RetailerStore():
    figure02 = create_pie()
    return render_template('RetailerStore.html', user = 2, plot=figure02, df_stores = df_stores)


@app.route('/Dashboard01')
def Dashboard01():
    return render_template('Dashboard01.html', user = 2)



def create_plot():
    fig01 = px.scatter(df, x='x', y='earnings', template="plotly_white", labels = {'x':'Month', 'earnings':'Earnings (CAD)'}, hover_data=["earnings"])
    fig01.update_xaxes(showgrid=False, zeroline=True)
    fig01.update_yaxes(showgrid=True, zeroline=False)
    fig01.update_traces(marker=dict(size=12, color='#ff8200'), hovertemplate=None )
    fig01.data[0].update(mode='markers+lines', line_shape='spline')
    fig01.update_layout(hovermode="x", hoverlabel=dict( font_color="white",  font_size=16, font_family="Rockwell"))
    # hoverlabel=dict( bgcolor="white",  font_size=16, font_family="Rockwell"))


    """
    fig01 = go.Scatter(x=df['x'], y=df['y'], mode='lines+markers',
                line=dict(color='#ff8200', width=4), line_shape='spline',
                marker=dict(color='#ff8200', size=10, symbol=0)

                )
    data = [fig01]

    data01 = go.Figure(
                data=[fig01],
                layout=go.Layout(
                    title=go.layout.Title(text="A Figure Specified By A Graph Object")
                    )
                )


    data02 = go.Figure(
                data=[fig01],
                layout=go.Layout(
                    xaxis= {'showgrid': False}
                    )
                )
    """

    graphJSON = json.dumps(fig01, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON



def create_pie():
    fig01 = px.pie(df_stores, values = 'Consumers',  names='Store')#, template="plotly_white", labels = {'x':'Month', 'earnings':'Earnings (CAD)'}, hover_data=["earnings"])
    #fig01.update_xaxes(showgrid=False, zeroline=True)
    #fig01.update_yaxes(showgrid=True, zeroline=False)
    #fig01.update_traces(marker=dict(size=12, color='#ff8200'), hovertemplate=None )
    #fig01.data[0].update(mode='markers+lines', line_shape='spline')
    fig01.update_layout(hovermode="x", hoverlabel=dict( font_color="white",  font_size=16, font_family="Rockwell"))


    graphJSON = json.dumps(fig01, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def create_pieProducts():
    fig01 = px.pie(df_HotProducts, values = 'Units',  names='Product', hover_data=["Earnings"])#, template="plotly_white", labels = {'x':'Month', 'earnings':'Earnings (CAD)'}, hover_data=["earnings"])
    fig01.update_layout(hovermode="x", hoverlabel=dict( font_color="white",  font_size=16, font_family="Rockwell"))


    graphJSON = json.dumps(fig01, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def create_plotProducts():
    fig01 = px.scatter(df_HotProducts, x='Product', y='Earnings', template="plotly_white", labels = {'x':'Month', 'earnings':'Earnings (CAD)'}, hover_data=["Earnings"])
    fig01.update_xaxes(showgrid=False, zeroline=True)
    fig01.update_yaxes(showgrid=True, zeroline=False)
    fig01.update_traces(marker=dict(size=12, color='#ff8200'), hovertemplate=None )
    fig01.data[0].update(mode='markers+lines', line_shape='spline')
    fig01.update_layout(hovermode="x", hoverlabel=dict( font_color="white",  font_size=16, font_family="Rockwell"))

    graphJSON = json.dumps(fig01, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
