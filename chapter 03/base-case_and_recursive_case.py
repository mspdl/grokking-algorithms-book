def regressive(start, end):
  print(start)
  if start <= end:
    return
  else:
    regressive(start-1, end)

regressive(10, 1)