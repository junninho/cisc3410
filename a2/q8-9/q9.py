from q8 import c_to_f
import plotly
import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
import pandas as pd

def cf_graph(temps):
  converted_temps = []

  for i in temps:
    converted_temps.append(c_to_f(i))

  fig = go.Figure()
  
  for i in range(len(temps)):
    arr1 = np.array(temps)
    arr2 = np.array(converted_temps)

    fig.add_trace(go.Scatter(
      x = arr2,
      y = arr1,
      mode = 'lines+markers',
      name = f'({temps[i]} C, {converted_temps[i]} F)'
    ))


  fig.update_layout(
    title = "Celsius vs Fahrenheit",
    xaxis_title = "Fahrenheit",
    yaxis_title = "Celsius"
  )

  pio.write_image(fig, 'q9.png')

def main():
  cels = [10, 25, 40, 55, 63, 78, 89, 100]
  cf_graph(cels)


if __name__ == '__main__':
    main()
