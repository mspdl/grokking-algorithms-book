states_to_cover = set(["rs", "sc", "pr", "sp", "mg", "es", "rj", "ms"])

stations = {}
stations["k-one"] = set(["sp", "mg", "rj", "es"])
stations["k-two"] = set(["rs", "sc", "pr", "sp"])
stations["k-three"] = set(["ms", "sp", "pr"])

final_stations = set()

best_station = None
covered_states = set()
for station, states_per_station in stations.items():
  covered = states_to_cover & states_per_station
  if len(covered) > len(covered_states):
    best_station = station
    covered_states = covered