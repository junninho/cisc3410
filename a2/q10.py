# This program solves the farmer, grain, goose, fox problem

'''
Character Code Reference
F = Farmer
G = Grain
E = Goose
X = Fox
'''

# Define position of characters in state list
char_pos = {
  'F': 0,
  'G': 1,
  'E': 2,
  'X': 3
}

# returns the result of an action on a given state
def get_result(state, action):
  new_state = state.copy()
  for char in action:
    new_state[char_pos.get(char)] = False if new_state[char_pos.get(char)] else True

  return new_state

# return if given state is valid
def is_state_valid(state):
  if state[1] == state[2]:
    if state[1] != state[0] and state[1] != state[3]:
      return False
  elif state[2] == state[3]:
    if state[2] != state[0] and state[2] != state[1]:
      return False
  if state[0] != state[1] and state[0] != state[2] and state[0] != state[3]:
    return False
  
  return True

# returns list of valid actions for given state
def get_valid_actions(state):
  all_actions = ['F', 'FG', 'FE', 'FX']
  valid_actions = []
  for action in all_actions:
    result = get_result(state, action)
    if is_state_valid(result):
      valid_actions.append(action)

  return valid_actions

# returns if given state matches the end goal
def is_goal_state(state):
  goal_state = [False, False, False, False]

  for i in range(len(state)):
    if state[i] != goal_state[i]:
      return False

  return True

# find a valid sequence of actions to solve the problem
def find_sequence(states, sequence):
  state = states[-1]
  actions = get_valid_actions(state)
  for action in actions:
    new_state = get_result(state, action)
    new_sequence = sequence.copy()
    new_sequence.append(action)

    if new_state in states:
      continue
    
    new_states = states.copy()
    new_states.append(new_state)

    if is_goal_state(new_state):
      return new_sequence
    else:
      seq = find_sequence(new_states, new_sequence)
      if seq:
        return seq
  
  return None

# main function
def main():
  states = [[True, True, True, True]] # list of states initialized with start state

  print(find_sequence(states, []))

if __name__ == '__main__':
    main()