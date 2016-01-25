## Cheering Mascot Challenge
##### Written in Python

### Rules
We are leading some cheers, and we have a mascot helping us by holding up signs that correspond to our cheers.  Here are the rules for how the mascot behaves.  While these rules might feel a little arbitrary, we are practicing writing to specifications.

-  The cheering only ends (i.e., the program exits) when we call out, "GAME OVER".

- Shouting is the only way for the mascot to hear us; we shout by typing in all caps.  If we shout out the name of a cheer, the mascot responds with the appropriate sign.  For example, if we call out for the "RED HOT" cheer, the mascot holds up the "H-O-T!" sign.

- If we call out a cheer without shouting, the mascot doesn't understand us and holds up a generic sign.  For example, if we call out for the "red hot" cheer, the mascot holds up the "Go Team!" sign.

- The mascot only knows a handful of cheers.  If we call out for a cheer the mascot doesn't know, it responds with the generic "Go Team!" sign.

  | KNOWN CHEER     | SIGN           |
  | :-------------: | :------------: |
  | RED HOT         | H-O-T!         |
  | DO IT AGAIN     | Go, Fight, Win |
  | 2 BITS          | Holler!        |
  | STOMP YOUR FEET | STOMP!         |

  *Table 1*.  Cheers known by the mascot and their corresponding signs.

-Program is run in the terminal.