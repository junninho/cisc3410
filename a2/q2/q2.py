import plotly
import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
import pandas as pd

def calculate_time(speed, distance):
  try:
    s = float(speed)
    d = float(distance)

    time = d/s
    print(f'Time: {time}')
    return time

  except ValueError:
    print("invalid Number")


def main():
  speed = []
  distance = []
  time = []

  for i in range(3):
    speed_in = input("Enter speed: ")
    distance_in = input("Enter distance: ")
    try:
      s = int(speed_in)
      d = int(distance_in)

      speed.append(s)
      distance.append(d)

      time.append(calculate_time(s, d))

    except ValueError:
      print("An invalid number was entered.")
  
  fig = go.Figure()
  
  for i in range(len(time)):
    x1 = [0, time[i]]
    y1 = [0, distance[i]]

    arr1 = np.array(x1)
    arr2 = np.array(y1)

    fig.add_trace(go.Scatter(
      x = arr1,
      y = arr2,
      text = f'Speed: {speed[i]}',
      mode = 'lines+markers',
      name = f'Speed: {speed[i]}'
    ))


  fig.update_layout(
    title = "Time vs Distance",
    xaxis_title = "Time",
    yaxis_title = "Distance"
  )

  pio.write_image(fig, 'q2.png')

if __name__ == '__main__':
    main()
    