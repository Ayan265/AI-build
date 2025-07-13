# quiz_game.py
def quiz():
    questions = [
        "How many Bones are in Human Body : ",
        "How many Continents in 2024 : ",
        "Full form of PPF : ",
        "Full form of AC : ",
        "Who invented Computer : ",
        "Closest Planet to Earth : "
    ]
    options = [
        ["A.205", "B.206", "C.207", "D.208"],
        ["A.8", "B.7", "C.6", "D.9"],
        ["A.Public Provident Finance", "B.Perfect Party Funds", "C.Passengers Passport Fraud", "D.Public Provident Fund"],
        ["A.Additional Current", "B.Alternating Current", "C.Andy Cart", "D.Alteration Current"],
        ["A.Charles Babbage", "B.Brain Tracy", "C.Swapna Willson", "D.Jackent Karyoune"],
        ["A.Mercury", "B.Venus", "C.Mars", "D.Moon"]
    ]
    answers = ["B", "B", "D", "B", "A", "A"]
    guesses = []
    score = 0

    for i in range(len(questions)):
        print("\n" + questions[i])
        for opt in options[i]:
            print(opt)
        guess = input("Your answer (A/B/C/D): ").upper()
        guesses.append(guess)
        if guess == answers[i]:
            print("CORRECT!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {answers[i]}")

    print("\n--- RESULT ---")
    print("Correct Answers:", " ".join(answers))
    print("Your Answers  :", " ".join(guesses))
    print(f"Score: {int(score/len(questions)*100)}%")
