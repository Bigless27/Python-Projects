def call_out_cheer():
  cheer = input('Enter a cheer: ')
  mascot_sign_for(cheer)

def display(cheer):
  print cheer

def mascot_sign_for(cheer):
  mascot_cheer = ""
  while cheer != "Game Over" :
    if cheer == "RED HOT":
      mascot_cheer = "H-O-T!"
    elif cheer == "DO IT AGAIN":
      mascot_cheer = "Go, Fight, Win"
    elif cheer == "2 BITS":
      mascot_cheer = "Holler!"
    elif cheer == "STOMP YOUR FEET":
      mascot_cheer = "STOMP!"
    else:
      mascot_cheer = "Go Team!"
    display(mascot_cheer)
  mascot_cheer = "Thanks for plaing!"
  display(mascot_cheer)

call_out_cheer()