import dash_html_components as html
import dash_core_components as dcc

headerComponent = html.Div(
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
        ], className='row twelve columns', style={'position': 'relative', 'right': '15px'}),

        html.Div([
            html.Code(
                '''
            ***Idminer*** is a tool that allows you to explore terms associated with query genes.
            The terms are extracted from articles related to the query gene obtained from parsing [PaperBLAST](http://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi) tool.
            '''
            )
        ])
    ])
