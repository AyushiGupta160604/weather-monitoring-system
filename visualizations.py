import plotly.graph_objs as go
from plotly.subplots import make_subplots

def plot_daily_temperatures(dates, avg_temps, max_temps, min_temps):
    fig = make_subplots(rows=1, cols=1)

    fig.add_trace(go.Scatter(
        x=dates,
        y=avg_temps,
        mode='lines+markers',
        name='Average Temp',
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=dates,
        y=max_temps,
        mode='lines+markers',
        name='Max Temp',
        line=dict(color='red')
    ))

    fig.add_trace(go.Scatter(
        x=dates,
        y=min_temps,
        mode='lines+markers',
        name='Min Temp',
        line=dict(color='green')
    ))

    fig.update_layout(
        title="Daily Temperature Trends",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        xaxis=dict(
            tickformat='%Y-%m-%d',  # Format the dates on the x-axis
            type="date",
        ),
        yaxis=dict(
            range=[min(min_temps), max(max_temps)]  # Set y-axis range
        ),
        legend=dict(title="Legend")
    )

    fig.show()
