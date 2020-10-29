import sys
import re
import json 
import requests

def first_requirement(gamers, count):
  ''' Print first <count> users '''
  try:
    result = gamers[0:count]
  except IndexError:
    print('Gamers count less, than you want, get all we have')
    print(json.dumps(gamers))
    return gamers  

  print(json.dumps(result))  
  return result


def second_requirement(gamers):
  '''Get info about <user_ id>'''
  try:         
    print(list(filter(lambda x: x['user_id'] == params_dict['user_id'], gamers)))
  except KeyError:
    print('User_id not found in commands or you entered wrong user_id')


def third_requirement(gamers):
  '''filter gamers with country we need, then count it'''
  try:  
    print(len(list(filter(lambda x: x['country'] == params_dict['country'], gamers))))
  except KeyError:
    print('Country not found or you entered wrong country code')


def get_request_params(params_dict):    
  URL = "https://www.diabotical.com/api/v0/stats/leaderboard"
  # game modes
  modes = ['r_macguffin', 'r_wo', 'r_rocket_arena_2',
           'r_shaft_arena_1', 'r_ca_2', 'r_ca_1']
  try:
    if params_dict['mode'] not in modes: # mode check
      print("Wrong game mode. See game modes:\n\
r_macguffin, r_wo, r_rocket_arena_2, r_shaft_arena_1, r_ca_2, r_ca_1")
      sys.exit(1)
  except KeyError:
    print("Mode game has not chosen! --mode MUST be in input")
    sys.exit(1)

  # send request
  get_request = requests.get(URL, params = {'mode': params_dict['mode']})

  if get_request.status_code == 200:    
    gamers = json.loads(get_request.text)["leaderboard"] 
    try:   
      # in 2 an 3 requirement see Count users
      get_count = int(params_dict['count'])
      if get_count < 1:
        raise ValueError
      gamers = first_requirement(gamers, get_count)
    except (KeyError, ValueError): 
      # if count wrong or empty select all gamers 
      print('Count N - is wrong or an empty command. Select all gamers.')
      print(json.dumps(gamers))
        
    if 'user_id' in params_dict.keys():
      # if user input include user_id - it requirement 2
      second_requirement(gamers)      
    elif 'country' in params_dict.keys():
      # if user input include country - it requirement 3
      third_requirement(gamers)    
  else:
    print(f'Status code is {get_request.status_code}\nAPI no respond, please try send request later')

      
def without_command_error():
  print('Enter commands: --mode <MODE>\n\
Optional: --count N, --user_id <user_id>, --country <country code>')
  sys.exit(1)

# tests
#params_dict = {'mode': 'r_wo', 'count': '4'}
#params_dict1 = {'mode': 'r_wo', 'count': '4', 'user_id': 'b04a64f68b9d4e36852105bd8a8f5266'}
#params_dict2 = {'mode': 'r_wo', 'count': '4', 'country': 'us'}

#get_request_params(params_dict)
#get_request_params(params_dict1)
#get_request_params(params_dict2)
    
 
if __name__ == "__main__":
  # NOTE: in this version in every Error we can see Error-message
  # then we quit the program (sys.exit(1))
  # we can change it by usage recursive call
  
  params_dict = {} #for non-positional command input    
  if len(sys.argv)>1: #we have any input from user        
    for i in range(1, len(sys.argv)):
      # command must start with '--'
      # after '--' should be at word
      # next argv is command parameter and not command
      try:
        if (re.match(r'--\w', sys.argv[i]) is not None and
            re.match(r'--\w', sys.argv[i+1]) is None):                        
            if sys.argv[i][2:] not in ['mode', 'count', 'user_id', 'country']:
              print("Unnknown command entered. See right commands below:")
              without_command_error()
            else:
              # add command without --
              params_dict[sys.argv[i][2:]] = sys.argv[i+1]                 
      except IndexError:
        print("Every command need a parameter. See right commands below:")
        without_command_error()
    # we must have commands from list
    if params_dict == {}:
      without_command_error()                
    get_request_params(params_dict)
  else:
    without_command_error()