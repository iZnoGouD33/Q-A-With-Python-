Questions = [
  {
    "prompt": "Which planet is known as the Red Planet?",
    "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    "answer": "C"
  },
  {
    "prompt": "Who wrote 'Romeo and Juliet'?",
    "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Leo Tolstoy"],
    "answer": "A"
  },
  {
    "prompt": "What is the largest ocean on Earth?",
    "options": ["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
    "answer": "B"
  },
  {
    "prompt": "Which gas do plants absorb from the atmosphere?",
    "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
    "answer": "B"
  },
  {
    "prompt": "Who developed the theory of relativity?",
    "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
    "answer": "B"
  }
]



def run_quiz(Questions):
    score = 0
    wrong_answer = 0
    right_answer = 0
    for question in Questions:
        print(question['prompt']) 
        for option in question['options']:
            print(option)
        answer = input('Enter your answer, (A, B, C or D, ):  ').capitalize()
        if answer == question['answer']:
            print("Correct!:\n")
            score+=5
            right_answer+=1
        else:
            print("Wrong!!! The correct answer was, ",question['answer'])
            wrong_answer +=1
    print(f"You Answered {right_answer} Questions right and {wrong_answer} Questions Wrong! Your Total Score is \n{score}")
run_quiz(Questions)