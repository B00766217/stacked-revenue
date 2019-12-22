# python africa_rev_stacked.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = pd.read_csv(
    "df_africa.csv"
)
#oper_options = df['Operation'].unique()
oper_options = ['All Operations','Directly Managed','HO Managed','National Operator']


app.layout = html.Div([
    html.H2(["Proposed 2020 Budgeted Revenue by Operational Unit"],style={'textAlign': "center", "padding-bottom": "30"}),
    html.Div(
        [
            dcc.Dropdown(
                id="Operation",
                options=[{
                    'label': i,
                    'value': i
                } for i in oper_options],
                value='All Operations'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='operations-graph'),
])


@app.callback(
    dash.dependencies.Output('operations-graph', 'figure'),
    [dash.dependencies.Input('Operation', 'value')])
def update_graph(Operation):
    if Operation == 'All Operations':
        df_plot = df.copy()
    else:
        df_plot = df[df['Operation'] == Operation]

    pv = pd.pivot_table(
        df_plot,
        index=['Territory_name'],
        columns=['Gl_description'],
        values=['2020B_amount'],
        aggfunc=sum,
        fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 1')], name='Module 1')
    trace2 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 2')], name='Module 2')
    trace3 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 3')], name='Module 3')
    trace4 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 4')], name='Module 4')
    trace5 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 5')], name='Module 5')
    trace6 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 6')], name='Module 6')
    trace7 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 7')], name='Module 7')
    trace8 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 8')], name='Module 8')
    trace9 = go.Bar(x=pv.index, y=pv[('2020B_amount', 'Module 9')], name='Module 9')


    return {
        'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9],
        'layout':
        go.Layout(
            title='{}'.format(Operation),
            barmode='stack')
    }


if __name__ == '__main__':
    app.run_server(debug=True)
