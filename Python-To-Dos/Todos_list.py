class Todos_list(object):
  def __init__(self):
    taskslist = open("todolist.txt",'r')
    taskarray = []
    for task in taskslist.readlines():
      taskarray.append(task.rstrip('\n'))
    self.taskarray = taskarray


  def add(self, item):
    self.taskarray.append(item)

  def delete(self, index):
    del self.taskarray[index - 1]

  def __repr__(self):
    lines = []
    for index, value in enumerate(self.taskarray):
      lines.append("{0}. {1}".format(index, value))
    return '\n'.join(lines)




tasks = Todos_list()
print tasks


