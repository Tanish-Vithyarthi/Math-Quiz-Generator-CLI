# Math-Quiz-Generator-CLI
A pyhton CLI tool for genrating random math quizzes.


# 🧠 Math Quiz Generator CLI

## Overview of the Project
This project is a **Command Line Interface (CLI) application** built using Python to provide a fast, interactive, and modular platform for practicing basic arithmetic skills. It aims to deliver immediate feedback to the user on their math abilities, addressing the lack of interactive practice tools.

## Features (Functional Modules)
The project includes the three major functional modules required:
* **Question Generator (`generator.py`):** Automatically creates random math problems (Addition, Subtraction, Multiplication).
* **Answer Validator (`validator.py`):** Takes user input, checks the correct answer, and provides instant feedback and **Error Handling**.
* **Score Tracker & Report (`tracker.py`):** Manages the quiz flow, tracks correct answers, and displays a final performance summary (Reporting or analytics).

## Technologies/Tools Used
* **Language:** Python 3.x
* **Libraries:** `random` (for question generation)
* **Version Control:** Git

## Steps to Install & Run the Project
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Tanish-Vithyarthi/Math-Quiz-Generator-CLI.git](https://github.com/Tanish-Vithyarthi/Math-Quiz-Generator-CLI.git)
    cd Math-Quiz-Generator-CLI
    ```
2.  **Modular Structure:** Ensure files are organized to meet the requirement of **minimum 5-10 modules/classes/files**:
    ```
    Math-Quiz-Generator-CLI/
    ├── src/ 
    │   ├── main.py        
    │   ├── generator.py  
    │   ├── validator.py   
    │   └── tracker.py     
    └── README.md
    └── statement.md
    ```
3.  **Run the application:**
    ```bash
    python src/main.py
    ```

## Instructions for Testing
The testing approach must include validation tests:
1.  Run the application and attempt all 5 questions.
2.  Test **Error Handling (Non-Functional Requirement)**: Enter text (e.g., "ten") instead of a number for an answer.The tool must handle this gracefully[span_6](end_span).
3.  Test **Reliability**: Ensure the score displayed at the end accurately reflects the number of correct answers.
