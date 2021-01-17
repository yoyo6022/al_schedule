import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import seaborn as sns
#import pandas_datareader.data as web
import datetime

df = pd.read_csv("~/Desktop/Springboard_Capstone3/data/train.csv")
sdf = pd.read_csv("~/Desktop/Springboard_Capstone3/data/combined_data.csv")
df.Date=pd.to_datetime(df.Date, format='%Y-%m-%d')
#print(df[:15])

# # https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )


# Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
# ************************************************************************
app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Rossmann Sales Dashboard",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

    dbc.Row([

        dbc.Col([
            html.P("Check Store Daily Sales:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn', multi=True, value='',
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['Store'].unique())],
                         ),
            dcc.Graph(id='line-fig', figure={})
        ], width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            html.P("Check Store Weekly Sales:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn2', multi=True, value='',
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['Store'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ], width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

    ], no_gutters=False, justify='start'),  # Horizontal:start,center,end,between,around

    dbc.Row([

        dbc.Col([
            html.P("Check Store Daily Customer:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn3', multi=True, value='',
                          options=[{'label':x, 'value':x}
                                   for x in sorted(df['Store'].unique())],
                         ),
            dcc.Graph(id='line-fig3', figure={}),
        ], width={'size':5, 'offset':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),


        dbc.Col([
            html.P("Check Store Daily Spend Per Customer",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn4', multi=True, value='',
                          options=[{'label':x, 'value':x}
                                   for x in sorted(df['Store'].unique())],
                         ),
            dcc.Graph(id='line-fig4', figure={}),
        ], width={'size':5, 'offset':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),


    ], no_gutters=False, justify='start'),  # Vertical: start, center, end

     dbc.Row([

        dbc.Col([
            html.P("Check Top 10 Sales of StoreType:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-dpdn5', multi=False, value='',
                          options=[{'label':x, 'value':x}
                                   for x in sorted(sdf['StoreType'].unique())],
                         ),
            dcc.Graph(id='bar-fig1', figure={}),
        ], width={'size':5, 'offset':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),


        dbc.Col([
            html.P("Check Store Daily Sales Histogram:",
                   style={"textDecoration": "underline"}),
            dcc.Dropdown(id='my-checklist', multi=True, value='',
                          options=[{'label':x, 'value':x}
                                   for x in sorted(df['Store'].unique())],
                         ),
            dcc.Graph(id='my-hist', figure={}),
        ], width={'size':5, 'offset':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        )


    ], no_gutters=False, justify='start'),



], fluid=True)


# Callback section: connecting the components
# ************************************************************************
# Line chart - multi daily sales
@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(storeid):
    dff = df[df['Store'].isin(storeid)].set_index('Date')
    figln = px.line(dff, x=dff.index, y='Sales', color='Store')
    return figln


# Line chart - multi weekly sales sum
@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph(storeid):
    dff = df[df['Store'].isin(storeid)].set_index('Date').Sales.resample('w').sum()
    figln2 = px.line(dff)
    return figln2



# line chart - customer
@app.callback(
    Output('line-fig3', 'figure'),
    Input('my-dpdn3', 'value')
)
def update_graph(storeid):
    dff = df[df['Store'].isin(storeid)].set_index('Date')
    figln3 = px.line(dff, x=dff.index, y='Customers', color='Store')
    return figln3



# line chart - sales per customer
@app.callback(
    Output('line-fig4', 'figure'),
    Input('my-dpdn4', 'value')
)
def update_graph(storeid):
    dff = df[df['Store'].isin(storeid)].set_index('Date')
    dff['SalesPerCustomer'] = dff['Sales']/dff['Customers']
    figln4 = px.line(dff, x=dff.index, y='SalesPerCustomer', color='Store')
    return figln4


@app.callback(
    Output('bar-fig1', 'figure'),
    Input('my-dpdn5', 'value')
)
def update_graph(storetype):
    sdff = sdf[sdf['StoreType']==storetype].sort_values('Sales', ascending=False).nlargest(10, 'Sales')
    #figln5 = go.Figure(go.Bar(x=sdff['Sales'], y=sdff['Store'].values.astype('str'),  orientation='h'))
    figbar1 = px.bar(x=sdff['Sales'], y=sdff['Store'].values.astype('str'),
                     labels={'y':'Store ID', 'x':'Total Sales'},  orientation='h')
    return figbar1



# Histogram
@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(storeid):
    dff = df[df['Store'].isin(storeid)]
    #dff = dff[dff['Store']==storeid]
    fighist = px.histogram(dff, x='Sales', nbins=10)
    return fighist


if __name__=='__main__':
    app.run_server(debug=True, port=8000)

