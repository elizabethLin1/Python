#Elizabeth Lin
#Word Jumble Program
#This game will give a random word(the order is random)from a list of words
#Then user need to guess the word

import random
#save some words which are chosen from the topic meteorology(Here use a tuple)
WORDS=("atmosphere","tornado","precipitation",
       "convection","avalanche")
HINTS=("It is all around the Earth", "It is a violently rotating column of air."
       ,"It is any product of the condensation of atmospheric water vapor that falls under gravity"
       ,"It si teh concerted, collective movement of groups or aggregates of molecules"
       +"within fluids.","It is a rapid flow of show down a sloping surface.")
#give hints to each word

#pick a word randomly using a random index
index=random.randint(0,len(WORDS)-1)
word=WORDS[index]
new_hint=HINTS[index]#match every word
#save a variable to save the shosen word in order that the while loop is work.
correct=word

#save a jumbled version of the word
Save_word=""#start with an empty string

while word: #the while loop runs until the word is the empty string
    position = random.randrange(len(word))
    Save_word += word[position]
    word = word[:position]+word[(position+1):]

#Start the game
#Intro.
print("We have a new game now!")
print("Word of Jumble!!!")
print("There will be a word with random characters.")
print("Your goal is to guess the word.")
print("Let's play now!")
print("The jumble is:",Save_word)

#Let user guess and check
count=0
guess=input("\nEnter your guess>")
count=count+1
while(guess!=correct and guess!=""):#when the answer is not correct, start while loop."
    print("Sorry, that's not it.")
    answer=input("Do you need a hint?")#ask users if they need a hint
    if answer=="yes":#if they need, print the hint.
        print(new_hint)#the hints is from the tuple.
 
    guess=input("\nEnter your guess>")
    count=count+1
    

if guess==correct:#when the guess is correct, the 
    print("That's the right answer. You get it.!!!")
    print("you take "+str(count)+ " times.")
else:
    print("This is the word you did not get.--"+correct)
print("Thanks for join us.")
input("\n\nPress ENTER to exit.")
