import dash_html_components as html
import dash_core_components as dcc
from src.components.header import headerComponent_configuration

uploadOrLoadSample = html.Div(
    className='flex-container',
    children=[
        dcc.Upload(
            id="upload-data",
            className='dashed-file-upload file-upload-50',
            children=html.Div(
                ["Upload file"]
            )),
        html.Button('Load Sample',
                    className='button-50'
                    )
    ]
)

generateNewRun = html.Div(
    children=[
        html.H4('Generate new run'),
        html.Div(
            className='flex-container',
            children=[
                dcc.Upload(
                    id="upload-file-to-process",
                    className='dashed-file-upload file-upload-50',
                    children=html.Div(
                        ["Upload data to process"]
                    )),
                dcc.RadioItems(
                    options=[
                        {'label': '.txt', 'value': 'TXT'},
                        {'label': '.fasta', 'value': 'FASTA'}
                    ],
                    value='TXT',
                    className='button-50'
                )
            ]
        ),
        html.Div(
            className='flex-container',
            children=[
                    html.Label('Keep Terms:'),
                    dcc.Textarea(
                        rows = 10,
                        id = 'list_keep_terms',
                        placeholder='Enter (one by line) terms which are frequent in english but you want to keep. See please see documentation to know wich term are in this categroy',
                        title='Optional field',
                        style={'align':'center'},
                        value='dominance\nsocial\nhead'
                                ),
                    html.Label('Remove Terms:'),
                    dcc.Textarea(
                        rows = 10,
                        id = 'list_remove_terms',
                        placeholder='Enter (one by line) terms which are frequent in english but you want to keep. See please see documentation to know wich term are in this categroy',
                        title='Optional field',
                        style={'align':'center'},
                        value='human\nplant\ncancer'
                                ),
            ]
        ),
        html.Div(
            children=[
                    html.Label('Zip-f Score:'),
                    dcc.Input(
                        placeholder='Enter a value between 0 and 8',
                        max = 8,
                        min = 0,
                        multiple = False,
                        size = 3,
                        type = 'number',
                        id = 'idf_score',
                        style={'align':'center'},
                        value=3.4
                    ),
                    html.Label('Max Number of Terms to Analyze:'),
                    dcc.Input(
                        placeholder='Enter a value between 0 and 10000',
                        max = 10000,
                        min = 0,
                        multiple = False,
                        size = 3,
                        type = 'number',
                        id = 'common_terms',
                        style={'align':'rigth'},
                        value=1000
                    )
            ],
        ),
        html.Label('Coverage %'),
        dcc.Slider(
            id='coverage-slider',
            className='login-slider',
            min=0,
            max=100,
            marks={i: f'{i}%' for i in range(0, 101, 10)},
            value=50,
            updatemode='drag'
        ),
        html.Label('Identity %'),
        dcc.Slider(
            id='identity-slider',
            className='login-slider',
            min=0,
            max=100,
            marks={i: f'{i}%' for i in range(0, 101, 10)},
            value=50,
            updatemode='mouseup'
        ),
          html.Button(
                    "Run",
                    id="run-btn",
                    
                )
    ]
)

layout = html.Div(
    id='configuration-form-container',
    children=[
        headerComponent_configuration,
        html.Hr(),
        html.H2('Configuration'),
        html.Div(
            id='login-container-centered',
            children=[
                uploadOrLoadSample,
                html.Hr(),
                generateNewRun
            ])
    ]
)


