import dash_table

PAGE_SIZE = 10


def termTable(pageSize, dfTerms):

    col = dfTerms.columns[:-1]
    print(col)
    return dash_table.DataTable(
        id='table-sorting-filtering',
        columns=[{"name": i, "id": i, 'deletable': True}
                 for i in dfTerms[col].columns],
        pagination_settings={
            'current_page': 0,
            'page_size': pageSize
        },
        pagination_mode='be',
        sorting='be',
        sorting_type='multi',
        sorting_settings=[],
        filtering='be',
        filtering_settings='',    
        style_table={'overflowX': 'scroll'},
        style_header={
            'backgroundColor': '#91B9E5',
            'fontWeight': 'bold',
            'font-family': 'Dosis',
            'textAlign': 'center',
            'font-size': '17'
        },
        style_cell={
            'backgroundColor': '#FAFAFA',
            'minWidth': '0px', 'maxWidth': '150px',
            'whiteSpace': 'no-wrap',
            'overflow': 'hidden',
            'textAlign': 'center',
            'padding': '5px',
            'font-size': '15'
        })


def geneTable(pageSize, df_genes_realtion):

    col = df_genes_realtion.columns

    return dash_table.DataTable(
        id='gene_table-sorting-filtering',
        columns=[{"name": i, "id": i, 'deletable': True}
                 for i in df_genes_realtion[col].columns],
        pagination_settings={
            'current_page': 0,
            'page_size': pageSize
        },
        pagination_mode='be',
        sorting='be',
        sorting_type='multi',
        sorting_settings=[],
        filtering='be',
        filtering_settings='',
        style_table={'overflowX': 'scroll'},
        style_header={
            'backgroundColor': '#91B9E5',
            'minWidth': '0px', 'maxWidth': '800px',
            'fontWeight': 'bold',
            'font-family': 'Dosis',
            'textAlign': 'center',
            'padding-right': '20px',
            'padding-left': '20px',
            'font-size': '15'
        },
        style_cell={
            'backgroundColor': '#FAFAFA',
            'minWidth': '0px', 'maxWidth': '800px',
            'whiteSpace': 'no-wrap',
            'overflow': 'hidden',
            'textAlign': 'center',
            'font-size': '15'
        })
