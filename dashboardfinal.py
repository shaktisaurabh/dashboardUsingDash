import plotly.graph_objs as go 
import dash 
from dash import dcc 
from dash import html 
import pandas as pd 

a1=pd.read_csv(r"C:\Users\LENOVO\Downloads\gapminder.csv") 
app=dash.Dash() 
app.layout=html.Div([
    html.Div(children=[html.H1("My first dashboard",style={'color':'red','text-align':'center'})],
                       style={'border':'1px black solid','float':'left','width':'100%',
                              'height':'50px'}),
    html.Div(children=[dcc.Graph(id='scatter-plot',figure={'data':[go.Scatter(x=a1['pop'],
                                                                              y=a1['gdpPercap'],
                                                                              mode='markers')],
                                                            'layout':go.Layout(title='Scatter plot')})]
        ,style={'border':'1px black solid','float':'left','width':'49.85%'}),
    html.Div(children=[dcc.Graph(id='box-plot',figure={'data':[go.Box(x=a1['gdpPercap'])],
                                                       'layout':go.Layout(title='Boxplot')})],
        style={'border':'1px black solid','float':'left','width':'49.85%'})
])

if __name__=='__main__':
    app.run_server(debug=True) 

#if you remove the height paramater from the 2nd Div then it will automatically adjust according to 
#the scatter plot