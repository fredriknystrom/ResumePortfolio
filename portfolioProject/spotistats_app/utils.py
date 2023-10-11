import plotly.express as px

def create_low_medium_high_pie_plot(data):
    names = ['Low', 'Medium', 'High']
    colors = ['#FF6961', '#F8D66D', '#8CD47E']
    fig = px.pie(values=data, names=names)

    fig.update_traces(
        hoverinfo='label',  # Only show the label when hovering
        hovertemplate='%{label}',  # Customize the hover label to show only the label
        textfont_size=16,
        marker=dict(colors=colors, line=dict(color='#222222', width=1))
    )

    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Set background color to transparent
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Set plot area background color to transparent
        font=dict(color='white'),  
        showlegend=False,
    )
    chart_html = fig.to_html(full_html=False, default_height=400, default_width=400)

    return chart_html