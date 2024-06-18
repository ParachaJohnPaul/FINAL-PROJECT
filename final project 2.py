def run_quiz(questions):
    user_answers = []
    score = 0

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        user_answer = input("Your answer: ")
        user_answers.append(user_answer)

        if user_answer.lower() == question['answer'].lower():
            score += 1

    return user_answers, score

def show_results(questions, user_answers, score):
    print("\nQuiz Results\n")
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        print(f"Your answer: {user_answers[i]}")
        print(f"Correct answer: {question['answer']}\n")

    print(f"Your total score is {score}/{len(questions)}")

def main():
    quiz_questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
        {"question": "What is the capital of Italy?", "answer": "Rome"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "What is the boiling point of water?", "answer": "100"},
        {"question": "What is the smallest prime number?", "answer": "2"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "Who wrote 'Hamlet'?", "answer": "Shakespeare"},
        {"question": "What is the speed of light in m/s?", "answer": "299792458"},]

    user_answers, score = run_quiz(quiz_questions)
    show_results(quiz_questions, user_answers, score)

if __name__ == "__main__":
    main()
