import tkinter as tk
from grades import GradeCalculator

class GradeCalculatorGUI:

    def __init__(self, root: tk.Tk, calculator: GradeCalculator):
        self.root = root
        self.calculator = calculator
        self._create_widgets()

    def _create_widgets(self):
        tk.Label(self.root, text="Total number of students:").pack()
        self.student_entry = tk.Entry(self.root)
        self.student_entry.pack()

        tk.Label(self.root, text="Enter scores (space-separated):").pack()
        self.scores_entry = tk.Entry(self.root)
        self.scores_entry.pack()

        self.submit_button = tk.Button(self.root, text="Calculate Grades", command=self._calculate_grades)
        self.submit_button.pack()

        self.grades_output = tk.Text(self.root, height=12)
        self.grades_output.pack()

    def _calculate_grades(self):
        num_students_str = self.student_entry.get()
        scores_str = self.scores_entry.get()


        result = self.calculator.process_inputs_and_calculate_grades(num_students_str, scores_str)

        self.grades_output.delete('1.0', tk.END)
        self.grades_output.insert(tk.END, result)



