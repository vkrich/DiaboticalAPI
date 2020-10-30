import json 
import requests
import argparse


URL = "https://www.diabotical.com/api/v0/stats/leaderboard"
  # game modes
modes = ['r_macguffin', 'r_wo', 'r_rocket_arena_2',
           'r_shaft_arena_1', 'r_ca_2', 'r_ca_1']


def remove_user_id(func):
  def wrapper(param):
    result = func(param)    
    if type(result) is int or result == 'Bad request or server unreachable':
      return result
    else:
      return json.dumps([{key: value for key, value in d.items() if key != 'user_id'} for d in result])
  return wrapper


@remove_user_id
def get_request(params): 
  try:
    get_request = requests.get(URL, params = {'mode': params.mode})
  except requests.exceptions.RequestException as e:
    raise SystemExit(e)

  if get_request.ok:    
    gamers = json.loads(get_request.text)["leaderboard"] 
     
    # in 2 an 3 requirement see Count users
    if params.count is not None:
      gamers = gamers[:params.count]

    if params.user_id is not None:
      # if user input include user_id - requirement 2
      return list(filter(lambda x: x['user_id'] == params.user_id, gamers))  
    elif  params.country is not None:
      # if user input include country - requirement 3       
      return len(list(filter(lambda x: x['country'] == params.country, gamers)))

    return gamers
  else:
    return 'Bad request or server unreachable'

      
def check_arguments(args):
  if args.mode not in modes:
    raise Exception("No such mode!")
  if args.count is not None and args.count < 1:
    raise Exception("Count number must be >= 1!")
  return True


if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('--mode', default='r_wo', action='store', type=str, nargs='?', required=True, help='Mode')
  parser.add_argument('--count', action='store', type=int, required=False, help='Count number')
  parser.add_argument('--user_id', action='store', nargs='?', type=str, required=False, help='User id')
  parser.add_argument('--country', action='store', nargs='?', type=str, required=False, help='Country symbol')
  args = parser.parse_args()
  check_arguments(args)

  print(get_request(args))