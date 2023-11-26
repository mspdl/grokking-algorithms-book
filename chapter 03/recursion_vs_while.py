def find_the_key_using_while(main_box):
  stack = main_box.create_stack_for_search()
  while stack is not empty:
    box = stack.take_box()
    for item in box:
      if item.is_a_box():
        stack.append(item)
      elif item.is_a_key():
        print("find the key!")

def find_the_key_using_recursion(main_box):
  for item in main_box:
    if item.is_a_box():
      find_the_key_using_recursion(item)
    elif item.is_a_key():
      print("find the key!")