import collections
import dash
import pandas as pd

from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import dash_html_components as html
import dash_core_components as dcc
import dash_table

app = dash.Dash(__name__)

df = pd.read_csv('last_export.csv', encoding='cp1251')



app.layout = html.Div([
    dcc.Store(id='memory-output'),
    dcc.Dropdown(id='memory-sensor', options=[
            {'value': 'BMP280_temp', 'label': 'temp'},
            {'value': 'BME280_humidity', 'label': 'humidity'},
        ], value='BMP280_temp'),
    html.Div([
        dcc.Graph(id='memory-graph'),
    ])
])


'''@app.callback(Output('memory-output', 'data'),
              [Input('memory-countries', 'value')])
def filter_countries(countries_selected):
    if not countries_selected:
        # Return all the rows on initial load/no country selected.
        return df.to_dict('records')

    filtered = df.query('country in @countries_selected')

    return filtered.to_dict('records')'''





@app.callback(Output('memory-graph', 'figure'),
              [Input('memory-output', 'data'),
               Input('memory-sensor', 'value')])
def on_data_set_graph(data, field):
    if data is None:
        raise PreventUpdate

    aggregation = collections.defaultdict(
        lambda: collections.defaultdict(list)
    )

    for row in data:

        a = aggregation[row['Date']]

        a['name'] = row['country']
        a['mode'] = 'lines+markers'

        a['x'].append(row[field])
        a['y'].append(row['temp'])

    return {
        'data': [x for x in aggregation.values()]
    }


if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=10451)