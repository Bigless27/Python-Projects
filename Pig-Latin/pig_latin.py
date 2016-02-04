class Pig_latin(object):
  vowels = ["a", "e" , "i", "o", "u", "A", "E", "I", "O", "U"]

  def __init__(self):
    self.sentence = raw_input("Enter a sentence to be converted into pig latin: ")
    print self.convert_sentence()

    while True:
      play_again = raw_input("Do you want to play again? Type yes or no: ").lower()
      if play_again == "yes":
        Pig_latin()
        break
      elif play_again == "no":
        print "thanks for playing!"
        break
      else:
        print "Please type yes or no!"

  def convert_sentence(self):
    new_sentence = self.sentence.split(" ")
    converted_sentence = []
    for word in new_sentence:
      if word[0] in self.vowels:
        converted_sentence.append(word)
      else:
        converted_sentence.append(''.join(self.word_converter(word)))
    return (' ').join(converted_sentence)

  def word_converter(self,word):
    solution = list(word)
    for letter in list(word):
      if letter not in self.vowels:
        solution.remove(letter)
        solution.append(letter)
      else:
        break
    solution.append("ay")
    return solution

Pig_latin()

