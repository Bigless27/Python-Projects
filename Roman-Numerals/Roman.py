from collections import OrderedDict

class Roman(object):

  def __init__(self, number):
    self.number = int(number)
    self.convert_table = self.make_table()

    while True:
      choice = raw_input("Type Yes or No for modern Roman Numeral Convert: ").lower()
      if choice == "yes":
        print "converted number = {0}".format(self.modern_roman_convert())
        print
        break
      elif choice == "no":
        print "converted number = {0}".format(self.old_roman_convert())
        print
        break
      else:
        print "Please Type Yes or No!"

    while True:
      play_again = raw_input("Do you want to enter another number? Please type yes or no: ").lower()
      if play_again == "no":
        print "thanks for playing"
        break
      elif play_again == "yes":
        Roman(raw_input("Enter another number! "))
        break
      else:
        print "Please Enter Yes or No!"

  def make_table(self):

    number = self.number
    convert_table = OrderedDict()
    while True:
      if number >= 1000:
        if "M" in convert_table:
          convert_table["M"] += 1
        else:
          convert_table["M"] = 1
        number -= 1000
      elif number >= 500:
        if "D" in convert_table:
          convert_table["D"] += 1
        else:
          convert_table["D"] = 1
        number -= 500
      elif number >= 100:
        if "C" in convert_table:
          convert_table["C"] += 1
        else:
          convert_table["C"] = 1
        number -= 100
      elif number >=50:
        if "L" in convert_table:
          convert_table["L"] += 1
        else:
          convert_table["L"] = 1
        number -= 50
      elif number >= 10:
        if "X" in convert_table:
          convert_table["X"] += 1
        else:
          convert_table["X"] = 1
        number -= 10
      elif number >= 5:
        if "V" in convert_table:
          convert_table["V"] += 1
        else:
          convert_table["V"] = 1
        number -= 5
      elif number >= 1:
        if "I" in convert_table:
          convert_table["I"] += 1
        else:
          convert_table["I"] = 1
        number -= 1
      else:
        break
    return convert_table


  def old_roman_convert(self):
    solution = []
    for key,value in self.convert_table.items():
      for i in range(0,value):
        solution.append(key)
    return ''.join(solution)


  def modern_roman_convert(self):
    solution = []
    reversed_list = OrderedDict(reversed(list(self.convert_table.items())))
    for key,value in reversed_list.items():

      if value < 4 and key == "I":
        for i in range(0,value):
          solution.append(key)
        continue
      elif value == 4 and key == "I":
        if "V" in reversed_list:
          solution.extend(("I","X"))
        else:
          solution.extend(("I","V"))
        continue

      if "V" == key and "V" not in solution and "X" not in solution:
        solution.append("V")

      if value < 4 and key == "X" :
        for i in range(0,value):
          solution.append(key)
        continue
      elif value == 4 and key == "X":
        if "L" in reversed_list:
          solution.extend(("C","X"))
        else:
          solution.extend(("L","X"))
        continue

      if "L" == key and "L" not in solution and "C" not in solution:
        solution.append("L")

      if value < 4 and key == "C" :
        for i in range(0,value):
          solution.append(key)
        continue
      elif value == 4 and key == "C":
        if "D" in reversed_list:
          solution.extend(("M","C"))
        else:
          solution.extend(("D","C"))
        continue

      if "D" == key and "M" not in solution and "D" not in solution:
        solution.append("D")

      if "M" == key:
        for i in range(0,value):
          solution.append("M")

    return ''.join(solution[::-1])


number = Roman(raw_input("Enter a number to be converted into Roman Numberal Form: "))

