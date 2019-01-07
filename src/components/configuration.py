import dash_html_components as html
import dash_core_components as dcc


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
            children=[
                    html.Label('Taxonomic Id:'),
                    dcc.Input(
                        placeholder='Enter a value...',
                        type='int',
                        value='50'
                    )
            ]
        ),
        html.Label('Coverage %'),
        dcc.Slider(
            id='my-range-slider',
            className='login-slider',
            min=0,
            max=100,
            step=1,
            value=50,
            marks={
                0: '0',
                100: '100'
            }
        ),
        html.Label('Identity %'),
        dcc.Slider(
            id='my-range-slider',
            className='login-slider',
            min=0,
            max=100,
            step=1,
            value=50,
            marks={
                0: '0',
                100: '100'
            }
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
