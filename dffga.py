import collections
import dash
import pandas as pd

from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import dash_html_components as html
import dash_core_components as dcc
import dash_table

def get_html_page(url):
    headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	}
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        html = None
    else:
        if r.ok:
            html = r.text
    return html

app = dash.Dash(__name__)

export_df = pd.read_csv('last_export.csv', delimiter=';', encoding='cp1251')

#print(export_df)

app.layout = html.Div(children=[
	html.H1(children='FLEX'),
	dcc.Graph(id='chart', animate=True),
	dcc.Interval(
		id='chart-update',
		interval=10*1000
	)
])




@app.callback(Output('chart', 'figure'), [Input('chart-update', 'n_intervals')])
def update_graph(input_data):
    export_df = pd.read_csv('last_export.csv', delimiter=';', encoding='cp1251')

    x_arr = []
    y_arr = []

    x_arr.append(line['Date'])
    y_arr.append((line['BMP280_temp']))

    traces = list()
    traces.append(plotly.graph_objs.Scatter(
        x=x_arr,
        y=y_arr,
        name='Scatter',
        mode='lines+markers'
    ))
    return {'data': traces}


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=10450)