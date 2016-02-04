class Pig_latin(object):
  vowels = ["a", "e" , "i", "o", "u", "A", "E", "I", "O", "U"]


  def __init__(self, sentence):
    self.sentence = sentence


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
    split_word = list(word)
    solution = list(word)
    for letter in split_word:
      if letter not in self.vowels:
        solution.remove(letter)
        solution.append(letter)
      else:
        break
    solution.append("ay")
    return solution





convert = Pig_latin("Hello eric ryan there")
print convert.convert_sentence()
