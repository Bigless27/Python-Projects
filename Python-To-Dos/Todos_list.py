class Todos_list(object):
  def __init__(self):
    taskarray = self.parse()
    self.taskarray = map(lambda task: Task(task), taskarray)


  def parse(self):
    taskslist = open("todolist.txt",'r')
    taskarray = []
    for task in taskslist.readlines():
      taskarray.append(task.rstrip('\n'))
    return taskarray

  def save(self):
    with open ("todolist.txt", "w") as text_file:
      for task in self.taskarray:
        text_file.write(task + "\n")

  def add(self, item):
    self.taskarray.append(item)
    self.save()

  def delete(self, index):
    del self.taskarray[index - 1]
    self.save()

  def __repr__(self):
    lines = []
    for index, value in enumerate(self.taskarray):
      lines.append("{0}. {1}".format(index, value))
    return '\n'.join(lines)




tasks = Todos_list()
print tasks


