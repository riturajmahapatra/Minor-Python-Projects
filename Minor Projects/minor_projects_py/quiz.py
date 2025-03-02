import random

def load_questions(filename="questions.txt"):
    questions = []
    with open(filename, "r") as file:
        for line in file:
            question, answer = line.strip().split("|")
            questions.append((question, answer.lower())) 
    return questions

print("Welcome to KBC \n - Hosted by - Rituraj")
playing = input("Are you ready to play a quick game? [y/N] ")

if playing.lower() != 'y':
    print("Okay, maybe next time!")
    quit()

print("\nOk, let's start!\n")    


questions = load_questions()
random.shuffle(questions) 


score = 0
for i, (question, correct_answer) in enumerate(questions, start=1):
    answer = input(f"Q{i}: {question} ").strip().lower()  
    if answer == correct_answer:
        print("✅ Correct! 🎉\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {correct_answer}\n")


print(f"Game Over! You got {score}/{len(questions)} correct.")    


### NEXT UPGRADE: include chatgpt question with this and add the KBC vibe