import random
import sys

def generate_question():
    """Generates a random math question (Addition, Subtraction, Multiplication)."""
    
    # Random numbers between 1 and 20 (for easier questions)
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    # Randomly select an operator
    operators = ['+', '-', '*']
    operator = random.choice(operators)

    # Calculate the correct answer based on the operator
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        # Ensures result is non-negative for basic quizzes
        if num1 < num2: 
            num1, num2 = num2, num1 # Swap numbers
        correct_answer = num1 - num2
    elif operator == '*':
        # Keep numbers smaller for multiplication (e.g., 1 to 10)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2

    question_text = f"What is {num1} {operator} {num2}? "
    return question_text, correct_answer

#  Answer Validator & Feedback ---
def validate_answer(user_input, correct_answer):
    """Validates user's answer and provides immediate feedback."""
    try:
        user_answer = int(user_input)
        if user_answer == correct_answer:
            print("✅ Correct!")
            return True, True # (Is Correct, Is Valid Number)
        else:
            print(f"❌ Incorrect. The correct answer was {correct_answer}.")
            return False, True # (Is Correct, Is Valid Number)
            
    except ValueError:
        # Error Handling: If user types text instead of a number
        print("❌ Invalid input. Please enter a whole number.")
        return False, False # (Is Correct, Is Valid Number)


# --- Functional Module 3: Score Tracker & Report (Main Function) ---
def start_quiz():
    """Starts the main quiz loop, tracks score, and generates the final report."""
    
    total_questions = 5  # Total questions in the quiz
    score = 0
    
    print("\n=====================================")
    print(f"🧠 MATH QUIZ: {total_questions} Questions")
    print("=====================================")

    for i in range(1, total_questions + 1):
        question_text, correct_answer = generate_question()
        
        # Loop to ensure a valid numeric input is received
        while True:
            # Ask the question
            user_input = input(f"Question {i}: {question_text}").strip()
            
            # Check for empty input (Skipped)
            if not user_input: 
                print("Skipped. Moving to next question.")
                break
                
            is_correct, is_valid_number = validate_answer(user_input, correct_answer)
            
            if is_valid_number:
                # If the input was a valid number (even if the answer was wrong), break the input loop
                if is_correct:
                    score += 1
                break
            else:
                # If the input was NOT a valid number (ValueError), the loop continues, asking again.
                continue

    # Final Score Report (Module 3 Output)
    print("\n============== RESULT ===============")
    print(f"Total Questions Attempted: {total_questions}")
    print(f"Correct Answers: {score}")
    final_percentage = int((score / total_questions) * 100) if total_questions > 0 else 0
    print(f"Your Score: {final_percentage}%")
    print("=====================================")
    

if __name__ == "__main__":
    start_quiz()