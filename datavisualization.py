from sklearn.neighbors import NearestNeighbors
import plotly.express as px
import numpy as np
from data_preprocess import preprocess_data

def visualize_data():
    data = preprocess_data()

    X = data.values
    print(data.values)
    nbrs = NearestNeighbors(n_neighbors=3)
    nbrs.fit(X)
    distances, indexes = nbrs.kneighbors(X)
    
    fig_1 = px.line(distances.mean(axis=1))
    fig_1.update_layout(showlegend=False)
    fig_1.update_xaxes(title_text="mean of k-distances", showgrid=False)
    fig_1.update_yaxes(title_text="", showgrid=False)
    fig_1.show()

    data["Points"] = 'normal'

    outlier_index = np.where(distances.mean(axis=1) > 35000)
    print(outlier_index)
    outlier_values = data.iloc[outlier_index]
    print(outlier_values)

    data["Points"].iloc[outlier_index] = "outlier"

    fig_2 = px.scatter(data, y=data["Weekly_Sales"], color="Points")
    fig_2.update_xaxes(showgrid=False)
    fig_2.update_yaxes(showgrid=False)
    fig_2.show()

    data.to_csv('walmart_cleansed_data.csv', index=False)
    
    return data
    

visualize_data()
