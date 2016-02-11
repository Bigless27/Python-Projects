class Todo_list(object):
  def __init__(self):
    list = open("todolist.txt",'r')
    for task in list.readlines():
      print task





