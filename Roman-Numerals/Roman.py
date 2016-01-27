class Roman(object):

  def __init__(self, number):
    self.number = int(number)
    choice = raw_input("Type Y or N for modern Roman Numeral Convert: ").lower()
    while True:
      if choice == "y":
        print "You made it"
      elif choice == "n":
        self.old_roman_convert()
        break
      else:
        print "Please Type Y or N!"
        (self, self.number)
    play_again = raw_input("Do you want to enter another number? Please type yes or no: ").lower()
    if play_again == "no":
      print "Thanks for Playing!"
    else:
      Roman(raw_input("Enter another number! "))


  def old_roman_convert(self):
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


number = Roman(raw_input("Enter a number to be converted into Roman Numberal Form: "))

