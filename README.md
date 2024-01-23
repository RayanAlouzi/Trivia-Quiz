# Quiz Application

This is a simple command-line quiz application that fetches questions from the Open Trivia Database API and allows users to answer them. The application is implemented in Python and consists of several files:

## Files

1. **data.py**: This file is responsible for fetching quiz questions from the Open Trivia Database API, processing the data, and creating a list of dictionaries containing questions and their corresponding correct answers.

2. **main.py**: The main script that initializes the quiz by creating a list of Question objects from the data obtained in `question_data`. It then uses the `QuizBrain` class to manage the quiz flow, presenting questions to the user and keeping track of their score.

3. **question_model.py**: Defines the `Question` class, representing a single quiz question. Each question has a text and an answer.

4. **quiz_brain.py**: Implements the `QuizBrain` class, which is responsible for managing the quiz flow, checking user answers, and keeping track of the score.

## Usage

1. Run the `main.py` file to start the quiz.

   ```bash
   python main.py
