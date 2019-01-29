import base64
import datetime
import io
import pandas as pd
import itertools
import math
from pathlib import Path
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import networkx as nx
import heapq
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
# from term_table import termTable


from src.components.header import headerComponent_dashboard




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.supress_callback_exceptions = True




app.layout = html.Div(
    className='flex-container',
    children=[
        dcc.Upload(
            id="upload-data",
            multiple=True,
            className='dashed-file-upload previous-file-upload-50',
            children=html.Div(
                ['Drag and Drop or ',html.A('Select Files')]
            )),
        html.Div(id='output-data-upload')
    ]
)



@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        if len(list_of_contents) ==2:
            for contents, names, dates in zip(list_of_contents, list_of_names, list_of_dates):
                if str(names).split("_")[-1] == "IDMiner-Terms.csv":
                    get_terms_df(contents, names, dates)
                    print(names)
                elif names.split("_")[-1] == "IDMiner-Genes.csv":
                    get_genes_df(contents, names, dates)
                    print(names)
                else:
                    return html.Div(['There was an error processing this file. You need to put both of this files, (yourname_IDMiner-Terms.csv,yourname_IDMiner-Genes.csv)'])
        else:
             return html.Div(['There was an error processing this file. You need to put BOTH (2) of this files, (yourname_IDMiner-Terms.csv,yourname_IDMiner-Genes.csv)'])
        children = [parse_contents(dfterms, dfgenesbyarticles)]
        return children



@app.callback(
    Output('table-sorting-filtering', 'data'),
    [Input('table-sorting-filtering', 'pagination_settings'),
     Input('table-sorting-filtering', 'sorting_settings'),
     Input('table-sorting-filtering', 'filtering_settings')])
def update_graph(pagination_settings, sorting_settings, filtering_settings):
    filtering_expressions = filtering_settings.split(' && ')
    col = dfterms.columns[:-1]
    dff = dfterms[col]
    for filter in filtering_expressions:
        if ' eq ' in filter:
            col_name = filter.split(' eq ')[0]
            filter_value = filter.split(' eq ')[1]
            dff = dff.loc[dff[col_name] == filter_value]
        if ' > ' in filter:
            col_name = filter.split(' > ')[0]
            filter_value = float(filter.split(' > ')[1])
            dff = dff.loc[dff[col_name] > filter_value]
        if ' < ' in filter:
            col_name = filter.split(' < ')[0]
            filter_value = float(filter.split(' < ')[1])
            dff = dff.loc[dff[col_name] < filter_value]

    if len(sorting_settings):
        dff = dff.sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1) *
        pagination_settings['page_size']
    ].to_dict('rows')


@app.callback(Output('net_graph', 'figure'), [Input('query-term-dropdown', 'value'), 
Input('union-intersection-dropdown', 'value')])
def load_graph(selected_dropdown_value, union_intersection):
    if len(selected_dropdown_value) > 0: #Cuando no tengo seleccion no hago nada. Para evitar que se generen vacios.
        graph = create_network(selected_dropdown_value,dfgenesbyarticles,union_intersection)
        if graph:
            return graph
        else:
            return {} 

if __name__ == '__main__':
    app.run_server(debug=True)
