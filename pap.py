import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


app = dash.Dash(__name__)

# Link external CSS file
app.css.append_css({"external_url": "styles.css"})

transparent_background_style = {'backgroundColor': 'rgba(0, 0, 0, 0)'}

# Load data from the Excel file for each sheet
df1 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet1")
df2 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet2")
df3 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet3")
df4 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet4")
df5 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet5")
df6 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet6")
df7 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet7")
df8 = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet8")
df_pesticides = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet9")
df_agricultural_inputs = pd.read_excel('C:\\Users\\educa\\Desktop\\Project Data deals.xlsx', sheet_name="Sheet11")

app.layout = html.Div([
    html.H1(" Seasonal agricultural Agricultural", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.P('Source of improved seeds(%)'),
            dcc.Dropdown(
                id='slicer-dropdown1',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Season A (2021)', 'value': 'Season A (2021)'},
                    {'label': 'Season B (2021)', 'value': 'Season B (2021)'},
                    {'label': 'Season C (2021)', 'value': 'Season C (2021)'},
                    {'label': 'Season A (2022)', 'value': 'Season A (2022)'},
                    {'label': 'Season B (2022)', 'value': 'Season B (2022)'},
                    {'label': 'Season C (2022)', 'value': 'Season C (2022)'},
                ],
                value='Season A (2021)'
            ),
            dcc.Graph(id='bar-plot1', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'}),

        html.Div([
            dcc.Dropdown(
                id='slicer-dropdown2',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Year(2020)', 'value': 'Year(2020)'},
                    {'label': 'Year(2021)', 'value': 'Year(2021)'},
                    {'label': 'Year(2022)', 'value': 'Year(2022)'},
                ],
                value='Year(2020)'
            ),
            dcc.Graph(id='bar-plot2', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'}, className="container"),

        html.Div([
            dcc.Dropdown(
                id='slicer-dropdown3',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Percentage of farmers', 'value': 'Percentage of farmers'},
                    {'label': 'Percentage of plots', 'value': 'Percentage of plots'},
                    {'label': 'Share of cultivated area', 'value': 'Share of cultivated area'},
                ],
                value='Percentage of farmers'
            ),
            dcc.Graph(id='bar-plot3', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%'},className="container"),
    ], style={'margin-bottom': '2%'}, className="graph-container"),

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='fertilizer-type',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[{'label': fertilizer, 'value': fertilizer} for fertilizer in
                         df8["Type of inorganic fertilizer used (%) in 2022"]],
                value='DAP'
            ),
            dcc.Graph(id='bar-plot4', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'},className="container"),

        html.Div([
            dcc.Dropdown(
                id='season-selector',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Season A', 'value': 'Season A'},
                    {'label': 'Season B', 'value': 'Season B'},
                ],
                value='Season A',
            ),
            dcc.Graph(id='bar-plot5', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'},className="container",),

        html.Div([
            dcc.Dropdown(
                id='season-dropdown',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[{'label': season, 'value': season} for season in df2['Seasonal'].unique()],
                value='Season A',
            ),
            dcc.Graph(id='bar-plot6', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%'},className="container"),
    ], style={'margin-bottom': '2%'},className="graph-container"),

    html.Div([
        html.Div([
            dcc.Dropdown(
                id='slicer-dropdown5',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Year(2021)', 'value': 'Year(2021)'},
                    {'label': 'Year(2022)', 'value': 'Year(2022)'},
                ],
                value='Year(2021)',
            ),
            dcc.Graph(id='bar-plot7', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'},className="container"),

        html.Div([
            dcc.Dropdown(
                id='slicer-dropdown6',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': 'Use of improved seeds per farmer', 'value': 'Use of improved seeds per farmer'},
                    {'label': 'Share of Land(%) in 2022', 'value': 'Share of Land(%) in 2022'},
                    {'label': 'Percentage(%) farmers', 'value': 'Percentage(%) farmers'},
                ],
                value='Use of improved seeds per farmer',
            ),
            dcc.Graph(id='bar-plot8', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%', 'margin-right': '2%'},className="container"),

        html.Div([
            html.H1("Pesticides per farmer"),
            html.Label("Select Year:"),
            dcc.Dropdown(
                id='year-dropdown',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[{'label': str(year), 'value': year} for year in df_pesticides['Year']],
                value=df_pesticides['Year'].max()
            ),
            dcc.Graph(id='bar-plot9', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ], style={'display': 'inline-block', 'width': '70%'},className="container"),
    ], style={'margin-bottom': '2%'},className="graph-container"),

    html.Div(
        style={'backgroundColor': '#f2f2f2', 'padding': '10px'},
        children=[
            html.H1("Agricultural Inputs", style={'textAlign': 'center'}),
            dcc.Dropdown(
                id='slicer-dropdown7',
                style={"width": "400px", "height": "50px", "backgroundColor": "white", "color": "black"},
                options=[
                    {'label': season, 'value': season}
                    for season in df_agricultural_inputs.columns[1:-1]  # Exclude the "Years" column
                ],
                value='Season A (2021)'
            ),
            dcc.Graph(id='bar-plot10', style={"width": "600px", "height": "400px", "textAlign": "centre"}),
        ]),
])

# ... (Your existing callbacks)
# First Callback - Update Stacked Bar Chart
@app.callback(
    Output('bar-plot1', 'figure'),
    [Input('slicer-dropdown1', 'value')]
)
def update_stacked_bar_chart(selected_season):
    years = df5['Years'].unique()
    data = []

    for year in years:
        selected_data = df5[df5['Years'] == year]
        data.append(go.Bar(
            x=selected_data['Source of improved seeds(%)'],
            y=selected_data[selected_season],
            name=str(year)
        ))

    layout = go.Layout(
        barmode='stack',
        xaxis={'title': 'Source of Improved Seeds (%)'},
        yaxis={'title': selected_season}
    )

    fig = go.Figure(data=data, layout=layout)
    return fig

# Second Callback - Update Bar Chart
@app.callback(
    Output('bar-plot2', 'figure'),
    [Input('slicer-dropdown2', 'value')]
)
def update_bar_chart(selected_year):
    fig = px.bar(
        df6,
        x='Percentage of farmers who applied fertilizer',
        y=selected_year,
        color='Seasonal',
        barmode='group',
        labels={'Percentage of farmers who applied fertilizer': 'Fertilizer Type'},
    )
    return fig

# Third Callback - Update Pie Chart
@app.callback(
    Output('bar-plot3', 'figure'),
    [Input('slicer-dropdown3', 'value')]
)
def update_pie_chart(selected_metric):
    filtered_df = df7[df7['Metric'] == selected_metric]

    fig = px.pie(
        filtered_df,
        names='Category',
        values='Value',
        title=selected_metric,
    )

    return fig

# Fourth Callback - Update Horizontal Bar Chart
@app.callback(
    Output('bar-plot4', 'figure'),
    [Input('fertilizer-type', 'value')]
)
def update_horizontal_bar_chart(selected_fertilizer):
    fig = go.Figure()
    selected_index = df8[df8["Type of inorganic fertilizer used (%) in 2022"] == selected_fertilizer].index[0]

    # Iterate through the bars and set different colors
    for i, season in enumerate(['Season A', 'Season B']):
        fig.add_trace(go.Bar(
            y=[season],
            x=[df8.loc[selected_index, season]],
            orientation='h',
            name=season,
        ))

    fig.update_layout(title=f"{selected_fertilizer} Usage in 2022", xaxis_title="Percentage")
    return fig
# Define callback to update Chart 1 based on the selected season
@app.callback(
    Output('bar-plot5', 'figure'),
    [Input('season-selector', 'value')]
)
def update_chart1(selected_season):
    fig = px.bar(
        df1, x="Agricultural land use (,000Ha) for 2022 Season A and B", y=selected_season,
        title=f"{selected_season} : Agricultural land use in 2022 Season A (in thousands of hectares)",
    )

    return fig

# Define callback to update Chart 2 based on the selected season
@app.callback(
    Output('bar-plot6', 'figure'),
    [Input('season-dropdown', 'value')]
)
def update_chart2(selected_season):
    filtered_df2 = df2[df2['Seasonal'] == selected_season]

    fig = px.bar(
        filtered_df2,
        x='Crop Type',
        y=['Year(2020)', 'Year(2021)', 'Year(2022)'],
        title=f'Crop Production for {selected_season}',
    )

    return fig

# Define callback to update Chart 3 based on the selected year
@app.callback(
    Output('bar-plot7', 'figure'),
    [Input('slicer-dropdown5', 'value')]
)
def update_chart3(selected_year):
    filtered_df3 = df3[df3[selected_year] > 0]
    fig = px.bar(
        filtered_df3,
        x='Seasonal',
        y=selected_year,
        color='Agricultural Input',
        barmode='group',
        labels={'Seasonal': 'Season'},
    )
    return fig

# Define callback to update Chart 4 based on the selected metric
@app.callback(
    Output('bar-plot8', 'figure'),
    [Input('slicer-dropdown6', 'value')]
)
def update_chart4(selected_metric):
    filtered_df4 = df4[df4['Category'] == selected_metric]
    fig = px.bar(
        filtered_df4,
        x='Metric',
        y=['Season A', 'Season B', 'Season C'],
        barmode='group',
        labels={'Metric': 'Category', 'value': selected_metric, 'variable': 'Season'},
    )
    return fig

# Callback to update the Pesticides bar chart based on the selected year
@app.callback(
    Output('bar-plot9', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_pesticides_chart(selected_year):
    filtered_df = df_pesticides[df_pesticides['Year'] == selected_year]
    fig = px.bar(filtered_df, x='Year', y=filtered_df.columns[2:], barmode='group')
    fig.update_layout(title=f"Pesticides Usage Data for {selected_year}")
    return fig
# Callback to update the Agricultural Inputs stacked bar plot based on the selected season
@app.callback(
    Output('bar-plot10', 'figure'),
    [Input('slicer-dropdown7', 'value')]
)
def update_agricultural_inputs_plot(selected_season):
    data = []
    legend_values = []  # Create a list to store legend values

    for year in df_agricultural_inputs.columns[1:-1]:  # Exclude the "Years" column
        data.append(go.Bar(
            x=df_agricultural_inputs['Source of improved seeds(%)'],
            y=df_agricultural_inputs[selected_season],
            name=year
        ))
        legend_values.append(year),

    layout = go.Layout(
        barmode='stack',
        xaxis={'title': 'Source of Improved Seeds (%)'},
        yaxis={'title': selected_season}
    )

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(legend_title_text=selected_season)  # Set legend title to selected season
    fig.update_layout(legend=dict(itemsizing="constant"))  # Ensure legend items have the same size
    fig.update_traces(marker=dict(opacity=0.7))  # Adjust legend marker opacity
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)
