import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import requests
import json
import csv
import pandas as pd




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

app.layout = html.Div(children=[
	html.H1(children='FLEX'),
	dcc.Graph(id='chart', animate=True),
	dcc.Interval(
		id='chart-update',
		interval=10*1000
	),
	dcc.Dropdown(id='memory-field', options=[
			{'value': 'lifeExp', 'label': 'json'},
			{'value': 'gdpPercap', 'label': 'csv'},
		], value='lifeExp')
])




@app.callback(Output('chart', 'figure'), [Input('chart-update', 'n_intervals')])
def update_graph(input_data):


	# load data

	x = 0
	x_arr = []
	y_arr = []




	'''with open('logger.txt', 'r', encoding="utf-8") as f:
		data = json.load(f)

		for item in data:
			if data[item]["uName"] == "Тест Студии":
				x_arr.append(x)
				y_arr.append(data[item]["data"]["BME280_temp"])
				x += 1'''

	file_name = 'last_export.csv'
	with open(file_name, 'r', encoding='cp1251') as f_obj:
		line = f_obj.readline()
		reader = csv.DictReader(f_obj, delimiter=';')

		for line in reader:
			x_arr.append(x)
			y_arr.append((line['BMP280_temp']))
			x += 1

	# create chart
	traces = list()
	traces.append(plotly.graph_objs.Scatter(
		x=x_arr,
		y=y_arr,
		name='Scatter',
		mode= 'lines+markers'
	))
	return {'data': traces}



if __name__ == '__main__':
	app.run_server(debug=True)
