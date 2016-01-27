from collections import defaultdict

class Roman(object):


  def __init__(self, number):
    self.number = int(number)
    self.convert_table = self.make_table()
    choice = raw_input("Type Y or N for modern Roman Numeral Convert: ").lower()
    while True:
      if choice == "y":
        print "You made it"
        break
      elif choice == "n":
        self.old_roman_convert()
        break
      else:
        print "Please Type Y or N!"
        (self, self.number)
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
    convert_table = defaultdict(int)
    while True:
      if number >= 1000:
        convert_table["M"] += 1
        number -= 1000
      elif number >= 500:
        convert_table["D"] +=1
        number -= 500
      elif number >= 100:
        convert_table["C"] += 1
        number -= 100
      elif number >=50:
        convert_table["L"] += 1
        number -= 50
      elif number >= 10:
        convert_table["X"] += 1
        number -= 10
      elif number >= 5:
        convert_table["V"] += 1
        number -= 5
      elif number >= 1:
        convert_table["I"] += 1
        number -= 1
      else:
        break
    return convert_table

  def old_roman_convert(self):
    print self.convert_table
    print "here"

    return


number = Roman(raw_input("Enter a number to be converted into Roman Numberal Form: "))

