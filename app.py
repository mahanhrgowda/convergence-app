import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

# Title
st.title("Convergence Point Visualizer with Big Bang Reference")

# Input year
year = st.number_input("Enter a year (BCE/CE, e.g., -5114 for 5114 BCE, 1993 for 1993 CE)", value=1993, step=1)

# Constants
BIG_BANG_YEARS = 13800000000  # 13.8 billion years
CURRENT_YEAR = 2025

# Calculate Z-value (time since Big Bang in billions of years)
def get_z_value(year):
    if year > 0:  # CE
        time_since_bb = BIG_BANG_YEARS - (CURRENT_YEAR - year) / 1e9
    else:  # BCE, year is negative
        time_since_bb = BIG_BANG_YEARS - (abs(year) + CURRENT_YEAR) / 1e9
    return time_since_bb

z_value = get_z_value(year)
st.write(f"Time since Big Bang for {year}: {z_value:.6f} billion years")

# Convergence points (adjusted for BCE and CE)
convergence_points = {
    -5114: "Rama’s Birth",
    -3228: "Krishna’s Birth",
    1956: "Suez Crisis",
    1993: "Your Birth",
    2067: "Future Convergence"
}

# 3D Plot using Plotly for interactivity
st.subheader("3D Helical Plot with Convergence Points")

# Generate helical paths
Z = np.linspace(-6000, 2100, 1000)  # Extended range for BCE and CE
phi = [0, 2*np.pi/3, 4*np.pi/3]  # Phase shifts for Śrī, Bhū, Nīlā
data = []
for i, color in enumerate(['yellow', 'orange', 'red']):
    X = 0.5 * np.sin(0.000001 * Z + phi[i])  # Small frequency for large range
    Y = 0.25 * np.cos(0.000001 * Z + phi[i])
    trace = go.Scatter3d(x=X, y=Y, z=Z, mode='lines', name=f'Devi {i+1}', line=dict(color=color))
    data.append(trace)

# Add convergence points
conv_points = []
for y, label in convergence_points.items():
    conv_points.append(go.Scatter3d(x=[0], y=[0], z=[y], mode='markers+text', name=label,
                                   marker=dict(symbol='x', size=10, color='red'),
                                   text=[label], textposition="top center"))

# Add input year marker
input_marker = go.Scatter3d(x=[0], y=[0], z=[year], mode='markers+text', name='Input Year',
                            marker=dict(symbol='circle', size=10, color='blue'),
                            text=[f'Year {year}'], textposition="top center")

data.extend(conv_points)
data.append(input_marker)

fig = go.Figure(data=data)
fig.update_layout(scene=dict(xaxis_title='Time Strand (-1 to 1)',
                             yaxis_title='Cosmic Flow (-1 to -0.25)',
                             zaxis_title='Year (BCE/CE)'),
                  title='Triple Helix Model with Convergence Points')
st.plotly_chart(fig)

# 2D Timeline Plot using Matplotlib
st.subheader("Timeline Plot with Convergence Points")

fig, ax = plt.subplots(figsize=(10, 6))
years = list(convergence_points.keys())
labels = list(convergence_points.values())
ax.plot(years, [0] * len(years), 'ro', label='Convergence Points')
ax.plot(year, 0, 'bo', label='Input Year')
for i, (y, label) in enumerate(zip(years, labels)):
    ax.text(y, 0.1, label, rotation=45, fontsize=8)
ax.text(year, -0.1, f'Year {year}', fontsize=8)
ax.set_xlabel('Year (BCE/CE)')
ax.set_ylabel('Convergence Level')
ax.set_title('Timeline of Convergence Points')
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Yantra Representation (Static Image Description)
st.subheader("Spiritual Yantra Representation")
st.write(f"The yantra, with a blue flame at the apex and Sanskrit text, symbolizes the spiritual convergence at {year} CE. Imagine a triangular design with nodes for Śrī, Bhū, and Nīlā Devī, set against a starry background, highlighting the cosmic alignment at {z_value:.6f} billion years since the Big Bang.")

# Additional Notes
st.write("Note: The visualizations are symbolic, with the Big Bang as the first convergence point. Scaling ancient dates is speculative, and interpretations may vary due to the blend of spiritual and scientific frameworks.")