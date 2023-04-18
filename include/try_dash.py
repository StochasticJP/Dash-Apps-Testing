import dash
from dash import html, dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output


# initialize dash app
app = dash.Dash()
df = px.data.stocks()  # read into stocks lib

# layout in html / css
# html.Div creates a div container in the app layout
app.layout = html.Div(id='parent', children = [

    # H1 title
    html.H1(id='H1', children='Styling using html components',
            style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}),

    # dropdown button
    dcc.Dropdown(id='dropdown', options=[{'label': 'Google', 'value': 'GOOG'},
                                         {'label': 'Apple', 'value': 'AAPL'},
                                         {'label': 'Amazon', 'value': 'AMZN'},
                                         ],
                 value = 'GOOG'),

    # graph itself
    dcc.Graph(id = 'line_plot', figure='')
])



@app.callback(Output(component_id='line_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_value):
    # function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x = df['date'], y = df['{}'.format(dropdown_value)],
                                line = dict(color = 'firebrick', width = 4))
                     ])
    fig.update_layout(title = 'Prices over time',
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )

    return fig



# main
if __name__ == '__main__':
    app.run_server()

