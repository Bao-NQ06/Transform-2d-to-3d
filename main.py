import streamlit as st
import numpy as np
import plotly.graph_objs as go
from transform import create_point_cloud_from_image
from PIL import Image
st.title("3D Object Viewer from Point Cloud")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.divider()

    try:
        point_cloud_data = create_point_cloud_from_image(uploaded_file)

        if not isinstance(point_cloud_data, np.ndarray) or point_cloud_data.shape[1] != 3:
            raise ValueError("Invalid point cloud data. Expected a NumPy array with shape (N, 3).")

        x, y, z = point_cloud_data[:, 0], point_cloud_data[:, 1], point_cloud_data[:, 2]

        fig_3d = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2,
                color=z,
                colorscale='Viridis',
                opacity=0.8
            )
        )])

        fig_3d.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z'
            ),
            margin=dict(l=0, r=0, b=0, t=0)  
        )

        st.write("3D Point Cloud")
        
        st.plotly_chart(fig_3d )
        
        st.divider()
        
        st.write("2D Image on 3D plane")
        
        image_array = np.array(image)
        height, width, _ = image_array.shape
        
        x = np.linspace(0, width, width)
        y = np.linspace(0, height, height)
        x, y = np.meshgrid(x, y)

        z = np.zeros_like(x)

        fig_2d = go.Figure(data=[go.Surface(
            z=z,
            x=x,
            y=y,
            surfacecolor=image_array[:, :, 0], 
            colorscale=None,
            showscale=False  
        )])

        fig_2d.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                aspectratio=dict(x=1, y=1, z=0.3)
            )
        )

        st.plotly_chart(fig_2d)

    except Exception as e:
        st.error(f"Error processing the image: {e}")
