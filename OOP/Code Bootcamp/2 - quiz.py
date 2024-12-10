import random
import time
print("Welcome to my quiz game! ")
score = 0
total_questions = 3
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Madrid', 'B. Rome', 'C. Paris', 'D. Berlin'],
        'answer': 'C'
    },
    {
        'question': 'Who wrote Romeo and Juliet?',
        'options': ['A. Charles Dickens', 'B. J.K. Rowling', 'C. Mark Twain', 'D. William Shakespeare'],
        'answer': 'D'
    },
    {
        'questions': 'What is the largest planet in our solar system?',
        'options': ['A. Earth', 'B. Jupiter', 'C. Uranus', 'D. Mars'],
        'answer': 'B'
    }
]
for question in questions:
    print(question['question'])
    for option in question['options']:
        print(option)
    guess = input("Choose an answer (A/B/C/D): ")
    if guess == question['answer']:
        print('Correct')
        score += 1
    else:
        score -= 1
        print('Incorrect')
    print()
    time.sleep(1)
