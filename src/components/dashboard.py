import dash
import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pathlib import Path
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import networkx as nx
import heapq

from app import app
from src.components.header import headerComponent
from src.components.term_table import termTable

#Separar archivo en tres

dfco = pd.read_csv("data/matrix.csv", sep=",", header=0, index_col=0)
dfterms = pd.read_csv("data/term-info.csv", sep=",",
                      header=0, low_memory=False)
dfgenesbyarticles = pd.read_csv(
    "data/Publications-by_gene.csv", sep=",", header=0, low_memory=False)

PAGE_SIZE = 10
# add weights to edges
edge_list = []
for index, row in dfco.iterrows():
    i = 0
    for col in row:
        weight = float(col)
        edge_list.append((index, dfco.columns[i], weight))
        i += 1

# Remove edge if 0 interactions
updated_edge_list = [x for x in edge_list if x[2] > 0]

try:
    query = dfterms[dfterms["Zipf_Score"] < 1].sort_values(
        "Articles", ascending=False).iloc[0]["Terms"]
except:
    query = dfterms.sort_values("Articles", ascending=False).iloc[0]["Terms"]

# network graph time
G = nx.Graph()

node_list = dfco.columns.tolist()

G.add_weighted_edges_from(updated_edge_list)


def get_network(G, query):
    H = nx.Graph(((t, g, w) for t, g, w in G.edges(
        data=True) if (g == query or t == query)))
    # Set node color based in articles
    nodecolor = dict([(v, e["weight"]) if (u == query) else (
        u, e["weight"]) for u, v, e in H.edges(data=True)])
    nodecolor[query] = 1
    nodecolorscale = dict([(v, e["weight"]) if (u == query) else (
        u, e["weight"]) for u, v, e in H.edges(data=True)])
    nodecolorscale[query] = 1
    maxinter = max(nodecolor.values())
    for node in nodecolorscale:
        nodecolorscale[node] = int((nodecolor[node]/maxinter)*100)

    nodecolorscale[query] = 0
    selected_nodes = list(H.nodes())
    selected_edges = list(H.edges())
    pos = nx.fruchterman_reingold_layout(H)

    Xed = []
    Yed = []
    for edge in selected_edges:
        Xed += [pos[edge[0]][0], pos[edge[1]][0], None]
        Yed += [pos[edge[0]][1], pos[edge[1]][1], None]

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        name='ntw',
        hoverinfo='text',
        marker=dict(symbol='circle-dot',
                    showscale=True,
                    # colorscale options
                    # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                    # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                    # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                    colorscale='YlOrRd',
                    reversescale=True,
                    color=[],
                    size=[],
                    colorbar=dict(
                        thickness=30,
                        title='Frequency in Articles',
                        xanchor='left',
                        titleside='right'),
                    )
    )

    for node in H.nodes():
        x, y = pos[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    annot = "IdMiner: Departamento de Genomica -IIBCE. " +\
        "<a href='http://www.genomica.weebly.com'> [1]</a>"

    for node in H.nodes():
        if node != query:
            node_info = node + ": " + str(int(nodecolor[node]))
            node_trace['marker']['color'] += tuple([int(nodecolorscale[node])])
            node_trace['marker']['size'] += tuple([70])
            node_trace['text'] += tuple([node_info])
        else:
            node_trace['marker']['color'] += tuple([0])
            node_trace['marker']['size'] += tuple([0])
            node_trace['text'] += tuple([""])

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                title=''
                )
    height = 800
    pubmed = "".join(dfterms[dfterms.Terms == query].Publications.tolist())
    link = "<a href=" + \
        "'https://www.ncbi.nlm.nih.gov/pubmed/{0}'".format(
            pubmed) + '>'+query.upper()+'</a>'
    title = link + ": # Genes: " + str(int(dfterms[(dfterms["Terms"] == query)]["Genes"].values)) + \
        " ; # Articles: " + \
        str(int(dfterms[(dfterms["Terms"] == query)]["Articles"].values))
    layout = go.Layout(title=title,
                       titlefont=dict(
                           family='Gadugi',
                           size=25,
                           color='black'
                       ),
                       font=dict(size=15),
                       plot_bgcolor='#EDEEF0',
                       showlegend=False,
                       autosize=True,
                       height=height,
                       xaxis=go.layout.XAxis(axis),
                       yaxis=go.layout.YAxis(axis),
                       margin=go.layout.Margin(
                           l=100,
                           r=100,
                           b=100,
                           t=100,
                       ),
                       annotations=[
                           dict(
                               showarrow=False,
                               text=query.upper(),
                               xref='paper',
                               yref='paper',
                               x=0,
                               y=-0.1,
                               xanchor='left',
                               yanchor='bottom',
                               font=dict(
                                   size=20
                               )
                           )
                       ]
                       )

    names_nodes = ["<a href=" + "'https://www.ncbi.nlm.nih.gov/pubmed/{0}'".format(str(dfgenesbyarticles[(dfgenesbyarticles["Terms"] == query)][str(
        x).replace(".0", "")].max()).replace(".0", "")) + 'style="color: #000000">' + x + "</a>" if x != query else "" for x in list(H.nodes())]
    names_trace = go.Scatter(
        x=node_trace["x"],
        y=node_trace["y"],
        text=names_nodes,
        hoverinfo='none',
        textposition='middle center',
        textfont=dict(
            family='arial',
            size=20,
            color='#000000'
        ),
        mode='text')

    data1 = [node_trace, names_trace]
    fig1 = go.Figure(data=data1, layout=layout)
    fig1['layout']['annotations'][0]['text'] = annot
    return fig1

f1 = get_network
layout = html.Div(children=[
    headerComponent,
    termTable(PAGE_SIZE, dfterms),
    dcc.Markdown('''#### Select Query Term:'''),

    html.Div(
        id='term-dropdown-container',
        children=[
            dcc.Dropdown(
                id='query-term-dropdown',
                options=[
                    {'label': i.title(), 'value': i} for i in sorted(dfterms.Terms.unique())
                ],
                multi=True,
                value=query
            ),
            dcc.Dropdown(
                id='union-intersection-dropdown',
                options=[
                    {'label': 'Union', 'value': 'UNION'},
                    {'label': 'Intersection', 'value': 'INTERSECTION'}
                ],
                value='UNION',
                searchable=False,
                clearable=False
            )
        ]
    ),
        dcc.Graph(id='net_graph'),
        dcc.Markdown('''#### Select Folder:''')
])


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


@app.callback(Output('net_graph', 'figure'), [Input('query-term-dropdown', 'value')])
def load_graph(selected_dropdown_value):
    return get_network(G, selected_dropdown_value)
