from plotly.graph_objects import Figure, Scatter3d

def scatter_3d(df, 
               x_col, y_col, z_col, size_col, color_col, 
               x_title, y_title, z_title, size_title, color_title, 
               color_scale=[0,1], scatter=0.01):

    from numpy import random, log

    fig = Figure(data=[Scatter3d(
        x=df[x_col] + random.normal(0, scatter, size=len(df)),
        y=df[y_col] + random.normal(0, scatter, size=len(df)),
        z=df[z_col] + random.normal(0, scatter, size=len(df)),
        mode='markers',
        marker=dict(
            size=log(df[size_col])*2+1,
            sizemode='diameter',
            opacity=0.8,
            color=df[color_col],
            colorscale='thermal',
            colorbar=dict(title=color_title),
            cmin=color_scale[0],
            cmax=color_scale[1]
        ),
        text=
            x_title + '=' + df[x_col].astype(str) + '; ' + 
            y_title + '=' + df[y_col].astype(str) + '; ' + 
            z_title + '=' + df[z_col].astype(str) + '; ' +
            size_title + '='+ df[size_col].astype(str),
        hoverinfo='text'
    )])

    fig.update_layout(
        title="Parametry i wyniki walidacji krzyżowej",
        margin=dict(l=0, r=0, b=0, t=0),
        scene=dict(
            xaxis_title=x_title,
            yaxis_title=y_title,
            zaxis_title=z_title
        )
    )
    
    return fig

def scatter_3d_params(df, scatter=0.01, color_scale=[0,1]):

    return scatter_3d(df, 
        'min_samples_leaf', 'min_samples_split', 'ccp_alpha', 'n_estimators', 'mean_test_score', 
        'Min.L', 'Min.S', 'A', 'ne', 'y', scatter = 0.01, color_scale=color_scale
    )