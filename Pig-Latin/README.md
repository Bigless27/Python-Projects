##Convert a sentance to piglatin

```text
FOR each word in the sentence.
  CONVERT SINGLE WORD to piglatin
ENDFOR
RETURN converted sentence
```
###Rules:
```text
- If the word starts with a vowel then return the word
- if the word starts with a consonant then remove the letter and append it to the end of the sentence
  - Do this until you hit a vowel then return the word with "ay" appended to it
- Finally return the converted sentence
```

###How to run application
-this application is run in the terminal using the python prefix
