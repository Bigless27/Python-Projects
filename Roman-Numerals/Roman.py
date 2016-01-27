from collections import OrderedDict

class Roman(object):


  def __init__(self, number):
    self.number = int(number)
    self.convert_table = self.make_table()
    print self.convert_table

    while True:
      choice = raw_input("Type Yes or No for modern Roman Numeral Convert: ").lower()
      if choice == "yes":
        print "You made it"
        break
      elif choice == "no":
        self.old_roman_convert()
        break
      else:
        print "Please Type Yes or No!"

    while True:
      play_again = raw_input("Do you want to enter another number? Please type yes or no: ").lower()
      if play_again == "no":
        print "Thanks for Playing!"
        break
      elif play_again == "yes":
        Roman(raw_input("Enter another number! "))
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
    print convert_table
    return table


  def old_roman_convert(self):
    solution = []
    dict(self.convert_table)
    table = OrderedDict(sorted(self.convert_table.items()))
    print table






    return


number = Roman(raw_input("Enter a number to be converted into Roman Numberal Form: "))

