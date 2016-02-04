class Pig_latin(object):
  vowels = ["a", "e" , "i", "o", "u", "A", "E", "I", "O", "U"]


  def __init__(self, sentence):
    self.sentence = sentence


  def convert_sentence(self):
    new_sentence = self.sentence.split(" ")
    converted_sentence = []
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
          converted_sentence.append(''.join(self.word_converter(word)))
          break
    return (' ').join(converted_sentence)


  def word_converter(self,word):
    split_word = list(word)
    solution = list(word)
    for letter in split_word:
      print letter
      if letter not in self.vowels:
        solution.remove(letter)
        solution.append(letter)
      else:
        break
    solution.append("ay")
    return solution





convert = Pig_latin("Hello there")
print convert.convert_sentence()
