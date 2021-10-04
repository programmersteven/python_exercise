def score_analyse(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif (score > 50) and (score <= 90):
            return "Passable"
        elif (score > 90) and (score <= 100):
            return "Excellent"
        elif score < 50:
            return "Bad"

def main():
    score = float(input("Enter score: "))
    print(score_analyse(score))

main()


import random

def random_score():
    return random.uniform(0,100)

print(random_score())