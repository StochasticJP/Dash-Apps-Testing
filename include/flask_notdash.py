from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart1')
def chart1():
    # data
    df = pd.DataFrame({'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                                 'Bananas'],
                       'Amount': [4, 1, 2, 2, 4, 5],
                       'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
                       })

    # plot the data
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)  # encode plotly to JSON

    header = "Fruit in North-America"
    description = "Amount of a specific fruit located in 2 cities"

    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart2')
def chart2():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Vegetables in Europe"
    description = """
    The rumor that vegetarians are having a hard time in London and Madrid can probably not be
    explained by this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


# main
if __name__ == "__main__":
    app.run()