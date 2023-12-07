class GradeCalculator:

    def determine_grade(self, score: int, best: int) -> str:
        if score >= best - (10/100)*best:
            return 'A'
        elif score >= best - (20/100)*best:
            return 'B'
        elif score >= best - (30/100)*best:
            return 'C'
        elif score >= best - (40/100)*best:
            return 'D'
        else:
            return 'F'

    def calculate_grades(self, scores: list[int]) -> tuple[list[str], float]:
        if not scores:
            raise ValueError("Score list is empty.")
        best = max(scores)
        grades = [self.determine_grade(score, best) for score in scores]
        average_score = sum(scores) / len(scores)
        return grades, average_score

    def process_inputs_and_calculate_grades(self, num_students_str: str, scores_str: str) -> str:
        try:
            num_students = int(num_students_str)
            if num_students <= 0:
                return "Error: Number of students must be positive."
        except ValueError:
            return "Error: Please enter a valid number for students."

        try:
            scores = [int(score) for score in scores_str.split()]
        except ValueError:
            return "Error: Please enter numbers only for scores."

        if len(scores) != num_students:
            return f"Error: Please enter grades for exactly {num_students} students."

        try:
            grades, average_score = self.calculate_grades(scores)
            best_possible_score = max(scores)  
            average_letter_grade = self.determine_grade(average_score, best_possible_score)
            grades_display = "\n".join(grades) + f"\n\nAverage Score: {average_score:.2f}"
            grades_display += f"\nAverage Grade: {average_letter_grade}"
            return grades_display
        except Exception as e:
            return f"Error: {str(e)}"
