class Todos_list(object):
  def __init__(self):
    taskslist = open("todolist.txt",'r')
    taskarray = []
    for task in taskslist.readlines():
      taskarray.append(task.rstrip('\n'))
    self.taskarray = taskarray


  def add(self, item):
    self.taskarray.append(item)
    print self.taskarray




tasks = Todos_list()
tasks.add("melons")

