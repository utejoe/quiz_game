def display_choices(choices):
    alphabet = ["A", "B", "C", "D"]
    for i in range(len(choices)):
        print(alphabet[i] + ") " + choices[i])

def display_final_score(score, total_questions):
    print("Quiz completed!")
    print("Your score:", score, "/", total_questions)