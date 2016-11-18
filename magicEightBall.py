import random

def  magicCycle():  
  number = random.randint(0,19)   
  if number == 0:
    answer = "It is certain"
  if number == 1:
    answer = "It is decidedly so"
  if number == 2:
    answer = "Without a doubt"
  if number == 3:
    answer = "Yes, definitely"
  if number == 4:
    answer = "You man rely on it"
  if number == 5:
    answer = "As I see it, yes"
  if number == 6:
    answer = "Most likely"
  if number == 7:
    answer = "Outlook good"
  if number == 8:
    answer = "Yes"
  if number == 9:
    answer = "Signs point to yes"
  if number == 10:
    answer = "Reply hazy try again"
  if number == 11:
    answer = "Ask again later"
  if number == 12:
    answer = "Better not tell you now"
  if number == 13:
    answer = "Cannot predict now"
  if number == 14:
    answer = "Concentrate and ask again"
  if number == 15:
    answer = "Don't count on it"
  if number == 16:
    answer = "My reply is no"
  if number == 17:
    answer = "My sources say no"
  if number == 18:
    answer = "Outlook not so good"
  if number == 19:
    answer = "Very doubtful"
  return answer  
  
def magicEightBall():
  quest=requestString("What would you like to ask the 8 ball?")
  answer = magicCycle()
  print answer
  repeat=requestString("Press any key and enter to roll again or type quit to quit the eight ball. Lastly if you'd like to ask a new question type new.")
  while repeat != "quit":
    if repeat == "new":
      resetBall()
    answer = magicCycle()
    print answer
    repeat=requestString("Press any key and enter to roll again or type quit to quit the eight ball. Lastly if you'd like to ask a new question type new.")
  if repeat == "quit":
    print "Thank you for visiting the magic eight ball. Have a nice day!"


def resetBall():
  magicEightBall()
    
  

    

