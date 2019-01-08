import dash_html_components as html
import dash_core_components as dcc

headerComponent_configuration = html.Div(
    [
        html.Div([
            html.Img(src='https://raw.githubusercontent.com/sradiouy/IdMiner/master/logo_transparent_background.png',
                     style={
                         'height': '100px',
                         'float': 'right',
                         'position': 'relative',
                         'bottom': '5px',
                         'left': '0px'
                     },
                     ),
            html.H2('IdMiner',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '10px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.H2('for',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '25px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '6.0rem',
                        'color': '#4D637F'
                    }),
            html.H2('Term Discovery',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '35px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.Hr(),
        ], className='row twelve columns', style={'position': 'relative', 'right': '15px'}),

        html.Div([
            html.H2(
                '''
            IDMINER is a tool that allows you to explore terms associated with query genes.
            The terms are extracted from articles related to the query gene obtained from parsing [PaperBLAST](http://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi) tool.
            ''',
            style={
                'position': 'relative',
                'top': '0px',
                'left': '25px',
                'font-family': 'Dosis',
                'display': 'inline',
                'font-size': '2.0rem',
                'color': '#000000'
                }
            )
                ])
    ])


headerComponent_dashboard = html.Div(
    [
        html.Div([
            html.Img(src='https://raw.githubusercontent.com/sradiouy/IdMiner/master/logo_transparent_background.png',
                     style={
                         'height': '100px',
                         'float': 'right',
                         'position': 'relative',
                         'bottom': '5px',
                         'left': '0px'
                     },
                     ),
            html.H2('IdMiner:',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '10px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.H2('for',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '25px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '6.0rem',
                        'color': '#4D637F'
                    }),
            html.H2('Term Discovery',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '35px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.Hr(),
        ], className='row twelve columns', style={'position': 'relative', 'right': '15px'}),

        html.Div([            
            html.H2(
                '''
            Discover relevant terms in your set of study genes through the exploration of the most relevant terms in the set of abstracts where the study genes (or homologs) are mentioned.

            ''',
            style={
                'position': 'relative',
                'top': '0px',
                'left': '25px',
                'font-family': 'Dosis',
                'display': 'inline',
                'font-size': '2.0rem',
                'color': '#000000'
                }
            ),
            html.Hr(),
        ])
    ])


headerComponent_geneboard = html.Div(
    [
        html.Div([
            html.Img(src='https://raw.githubusercontent.com/sradiouy/IdMiner/master/logo_transparent_background.png',
                     style={
                         'height': '100px',
                         'float': 'right',
                         'position': 'relative',
                         'bottom': '5px',
                         'left': '0px'
                     },
                     ),
            html.H2('IdMiner:',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '10px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.H2('Genes Relations',
                    style={
                        'position': 'relative',
                        'top': '0px',
                        'left': '35px',
                        'font-family': 'Dosis',
                        'display': 'inline',
                        'font-size': '7.0rem',
                        'color': '#4D637F'
                    }),
            html.Hr(),
        ], className='row twelve columns', style={'position': 'relative', 'right': '15px'}),

        html.Div([
            
            html.H2(
                '''
            In this section you can explore the relationships between your query genes. In the table you can see how many articles in common have two genes given. While in the network you can select all the articles that are related to the query gene, and also, selecting a node (from the network) you can see the articles that have in common the selected node (subject gene) and the query gene.

            ''',
            style={
                'position': 'relative',
                'top': '0px',
                'left': '25px',
                'font-family': 'Dosis',
                'display': 'inline',
                'font-size': '2.0rem',
                'color': '#000000'
                }
            ),
            html.Hr(),
        ])
    ])
