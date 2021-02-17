# import libraries

from q8 import c_to_f # import celsius to fahrenheit function from q8
import plotly
import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
import pandas as pd

# define graphing function
def cf_graph(temps):
  converted_temps = [] # list to store converted temps

  # for each temp convert to celsius and append to converted temp array
  for i in temps:
    converted_temps.append(c_to_f(i))

  # create figure
  fig = go.Figure()
  
  # for each temp, create numpy array
  for i in range(len(temps)):
    arr1 = np.array(temps)
    arr2 = np.array(converted_temps)

    # add trace to figure
    fig.add_trace(go.Scatter(
      x = arr2,
      y = arr1,
      mode = 'lines+markers',
      name = f'({temps[i]} C, {converted_temps[i]} F)'
    ))

  # update figure with celsius
  fig.update_layout(
    title = "Celsius vs Fahrenheit",
    xaxis_title = "Fahrenheit",
    yaxis_title = "Celsius"
  )

  # create image of graph
  pio.write_image(fig, 'q9.png')

def main():
  cels = [10, 25, 40, 55, 63, 78, 89, 100] # sample array
  cf_graph(cels) # call function with above array


if __name__ == '__main__':
    main()
