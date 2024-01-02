from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('dash_learn/gapminder2007.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg')),
    dcc.Graph(figure=px.histogram(df, x='lifeExp'))
])


if __name__ == '__main__':
    app.run(debug=True)
