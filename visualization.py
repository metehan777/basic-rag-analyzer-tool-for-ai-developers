from typing import List
import plotly.graph_objects as go

def plot_similarity_scores(similarity_scores: List[float]):
    """Create a bar chart of similarity scores."""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=[f"Result {i+1}" for i in range(len(similarity_scores))],
        y=similarity_scores,
        marker_color='rgb(26, 118, 255)',
        name='Similarity Score'
    ))

    fig.update_layout(
        title='Similarity Scores for Query Results',
        xaxis_title='Results',
        yaxis_title='Similarity Score',
        yaxis_range=[0, 1],
        template='plotly_white',
        showlegend=False
    )

    return fig
