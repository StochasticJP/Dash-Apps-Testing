# Flask + Plotly lib to recreate try_dash.py

from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)  # create a flask app

# route to home '/' - Flask URLs are mapped onto functions and the decorator tells us which function
# corresponds to a particular url


@app.route('/')  # decorator and shows what you want to show (same as react routing)
def notdash():
    # create data using panda dataframes type
    df = pd.DataFrame({'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
      'Bananas'],
                       'Amount': [4, 1, 2, 2, 4, 5],
                       'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
                       })

    # create a fig and populate with data
    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

    # convert the plot to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # flask to use a html template of notdash and pass the JSON code to it
    return render_template('notdash.html', graphJSON=graphJSON)


# main
if __name__ == '__main__':
    app.run()