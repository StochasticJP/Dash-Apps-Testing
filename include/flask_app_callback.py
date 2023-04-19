from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)


@app.route('/callback', methods=['POST', 'GET'])   # call back route using POST-GET methods
def cb():
    return gm(request.args.get('data'))  # callback returns gm functions with input args


@app.route('/')
def index():
    return render_template('chartsajax.html', graphJSON=gm())  # show default JSON graph


def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())

    fig = px.line(df[df['country']==country], x="year", y="gdpPercap")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


# main
if __name__ == "__main__":
    app.run()
