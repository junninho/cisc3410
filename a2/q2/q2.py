# import necessary libraries
import plotly
import plotly.graph_objs as go
import plotly.io as pio
import numpy as np
import pandas as pd

# define function to calculate time given time and distance
def calculate_time(speed, distance):
  # test and catch errors
  try:
    # convert parameter values to float
    s = float(speed)
    d = float(distance)

    time = d/s # calculate time
    print(f'Time: {time}')
    return time # return value of time

  # if valueError is returned, print message
  except ValueError:
    print("invalid Number")

# main function
def main():
  # initialize variables to store array of values
  speed = [100, 85, 92]
  distance = [100, 100, 100]
  time = []

  # loop 3 times
  for i in range(len(speed)):
    # check that same number of values are in both arrays
    if (len(speed) != len(distance)):
      print("Speed and Distance arrays need to be the same length")
      return -1 # end program if lengths are not equal

    # convert values to integer and calculate time
    try:
      s = int(speed[i])
      d = int(distance[i])
      time.append(calculate_time(s, d)) # append to time array

    except ValueError:
      print("An invalid number was entered.")
  
  # create figure
  fig = go.Figure()
  
  # plot the values in the time and distance arrays
  for i in range(len(time)):
    x1 = [0, time[i]]
    y1 = [0, distance[i]]

    # convert arrays to numpy arrays used for plotting
    arr1 = np.array(x1)
    arr2 = np.array(y1)

    # add line to graph
    fig.add_trace(go.Scatter(
      x = arr1,
      y = arr2,
      text = f'Speed: {speed[i]}',
      mode = 'lines+markers',
      name = f'Speed: {speed[i]}'
    ))

  # update layout to add title and axis labels
  fig.update_layout(
    title = "Time vs Distance",
    xaxis_title = "Time",
    yaxis_title = "Distance"
  )

  # write graph to file
  pio.write_image(fig, 'q2.png')

if __name__ == '__main__':
    main()
    