voted = {}

def check_voter(name):
  print("Checking " + name + "'s vote...")
  if(voted.get(name)):
    print("Already voted. Send away!")
  else:
    print("Allowed to vote.")
    voted[name] = True
  print("=== Ended ===")

check_voter("Tom")
check_voter("Mike")
check_voter("Morgan")
check_voter("Mike")
check_voter("Tom")