def Madlibs():
  print("Let's play a game of Madlibs!")

  name = str(input("Enter your name: "))
  adjective = str(input("Enter adjective ..: "))
  animal = str(input("Enter animal name: "))
  silly_word = str(input("Enter silly word: "))
  verb_ending_in_ing = str(input("Enter verb_ending_in_ing: "))
  place = str(input("Enter place name:"))
  funny_sound = str(input("Enter funny sound: "))
  plural_noun = str(input("Enter plural noun: "))
  emotion = str(input("Enter emotion: "))
  


  story = f""" \n One day, {name} woke up feeling very {adjective}.
 Outside the window, a giant {animal} was doing the {silly_word} dance.
 Without thinking, {name} started {verb_ending_in_ing} all the way to {place}.
 Suddenly, there was a loud {funny_sound}!Out came a gang of wild {plural_noun},
 all wearing hats made of flowers.{name} felt so {emotion}, but still whispered, “Best. Day. Ever.” """
  
  
  print(story)

if __name__ == "__main__":
    Madlibs()





