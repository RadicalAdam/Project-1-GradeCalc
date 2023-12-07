import tkinter as tk
from gui import GradeCalculatorGUI
from grades import GradeCalculator

def main():

    root = tk.Tk()
    root.title("Grade Calculator")
    
    calculator = GradeCalculator()
    gui = GradeCalculatorGUI(root, calculator)
    
    root.mainloop()

if __name__ == "__main__":
    main()
