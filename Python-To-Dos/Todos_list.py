class Todos_list(object):
  def __init__(self):
    taskslist = open("todolist.txt",'r')
    taskarray = []
    for task in taskslist.readlines():
      taskarray.append(task.rstrip('\n'))
    print taskarray




Todos_list()
