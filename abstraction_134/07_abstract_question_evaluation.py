"""
Abstraction - Program 7:
Create an abstract class Question with an abstract method evaluate_answer().
Derive:
a) MCQQuestion
b) TrueFalseQuestion
c) DescriptiveQuestion
Implement answer evaluation for each question type.
"""

from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question_text, max_marks):
        self.question_text = question_text
        self.max_marks = max_marks

    @abstractmethod
    def evaluate_answer(self, submitted_answer):
        """Evaluates student's answer and returns (marks_awarded, feedback)."""
        pass

    def display_question(self):
        print(f"Q: {self.question_text} [{self.max_marks} Marks]")


class MCQQuestion(Question):
    def __init__(self, question_text, options, correct_option_key, max_marks=2):
        super().__init__(question_text, max_marks)
        self.options = options  # dict: {'A': ..., 'B': ...}
        self.correct_option_key = correct_option_key.upper()

    def display_question(self):
        super().display_question()
        for key, text in self.options.items():
            print(f"   ({key}) {text}")

    def evaluate_answer(self, submitted_answer):
        submitted = str(submitted_answer).strip().upper()
        if submitted == self.correct_option_key:
            return self.max_marks, "Correct option selected."
        else:
            return 0, f"Incorrect. Correct answer was ({self.correct_option_key})."


class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_boolean, max_marks=1):
        super().__init__(question_text, max_marks)
        self.correct_boolean = bool(correct_boolean)

    def evaluate_answer(self, submitted_answer):
        if isinstance(submitted_answer, str):
            submitted_bool = submitted_answer.strip().lower() in ["true", "t", "1", "yes"]
        else:
            submitted_bool = bool(submitted_answer)

        if submitted_bool == self.correct_boolean:
            return self.max_marks, f"Correct! The statement is indeed {self.correct_boolean}."
        else:
            return 0, f"Incorrect! The statement is {self.correct_boolean}."


class DescriptiveQuestion(Question):
    def __init__(self, question_text, key_keywords, max_marks=5):
        super().__init__(question_text, max_marks)
        self.key_keywords = [k.lower() for k in key_keywords]

    def evaluate_answer(self, submitted_answer):
        text = str(submitted_answer).lower()
        matched = [k for k in self.key_keywords if k in text]
        score_ratio = len(matched) / len(self.key_keywords) if self.key_keywords else 1.0
        awarded_marks = round(score_ratio * self.max_marks, 1)
        feedback = f"Matched {len(matched)}/{len(self.key_keywords)} key concepts: {matched}"
        return awarded_marks, feedback


if __name__ == "__main__":
    q1 = MCQQuestion(
        "Which of the following data types in Python is immutable?",
        {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"},
        correct_option_key="C"
    )

    q2 = TrueFalseQuestion(
        "Python supports multiple inheritance directly.",
        correct_boolean=True
    )

    q3 = DescriptiveQuestion(
        "Explain the core purpose of encapsulation in object-oriented programming.",
        key_keywords=["data hiding", "security", "private", "access"],
        max_marks=5
    )

    assessment = [
        (q1, "C"),
        (q2, "False"),
        (q3, "Encapsulation achieves data hiding and security by making attributes private and controlling access.")
    ]

    print("=== Automated Exam Grading Engine (Abstraction Interface) ===")
    total_score = 0
    max_score = 0
    for q, ans in assessment:
        print()
        q.display_question()
        print(f"Submitted Answer: \"{ans}\"")
        marks, remark = q.evaluate_answer(ans)
        print(f"Result: {marks} / {q.max_marks} Marks | Feedback: {remark}")
        total_score += marks
        max_score += q.max_marks

    print("=" * 60)
    print(f"Final Candidate Score: {total_score} / {max_score}")
