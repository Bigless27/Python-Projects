class Roman(object):

  def __init__(self, number):
    self.number = number
    self.modern_convert()
    convert_table = {}

  def modern_convert(self):
    number = self.number
    solution = []
    while True:
      if number >= 1000:
        solution.append("M")
        number -= 1000
      elif number >= 500:
        solution.append("D")
        number -= 500
      elif number >= 100:
        solution.append("C")
        number -= 100
      elif number >=50:
        solution.append("L")
        number -= 50
      elif number >= 10:
        solution.append("X")
        number -= 10
      elif number >= 5:
        solution.append("V")
        number -= 5
      elif number >= 1:
        soution.append("I")
        number -= 1
      else:
        break
    print "".join(solution)
    return


number = Roman(15)

