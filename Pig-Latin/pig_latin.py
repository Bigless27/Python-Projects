class Pig_latin(object):
  vowels = ["a", "e" , "i", "o", "u"]


  def __init__(self, sentence):
    self.sentence = sentence

  def convert_sentence(self):
    new_sentence = self.sentence.split(" ")
    for word in new_sentence:
      counter = 0
      if word[0] in self.vowels:
        continue
      for letter in word:
        if counter == 1:
          continue
        if letter in self.vowels:
          counter += 1
        else:
          pass


convert = Pig_latin("Hello there")
convert.convert_sentence()
