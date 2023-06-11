"""Rhys Sheehan CP1404 Prac 2 score.py"""


def main():
    score = float(input("Enter score: "))
    print(score_result(score))


def score_result(score):
    if score > 50:
        return "Passable"
    if score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"
    else:
        if score <= 0 or score > 100:
            return "Invalid score"


main()
