import tkinter as tk
import random
import time


class MathQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Математический квиз на скорость")

        self.score = 0
        self.time_limit = 30
        self.start_time = None

        self.question_label = tk.Label(root, font=("Arial", 24))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root, font=("Arial", 24))
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Ответить", command=self.check_answer, font=("Arial", 24))
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="Очки: 0", font=("Arial", 18))
        self.score_label.pack()

        self.timer_label = tk.Label(root, text="Время: 30", font=("Arial", 18))
        self.timer_label.pack()

        self.answer_entry.bind("<Return>", lambda event: self.check_answer())

        self.start_game()

    def start_game(self):
        self.score = 0
        self.time_limit = 30
        self.start_time = time.time()
        self.update_timer()
        self.generate_question()

    def update_timer(self):
        time_left = self.time_limit - (time.time() - self.start_time)
        if time_left > 0:
            self.timer_label.config(text=f"Время: {int(time_left)}")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            self.answer = num1 + num2
        elif operation == '-':
            self.answer = num1 - num2
        elif operation == '*':
            self.answer = num1 * num2
        else:  # Деление
            # Чтобы деление было целым, умножаем num1 на num2
            num1 *= num2
            self.answer = num1 // num2

        self.question_label.config(text=f"{num1} {operation} {num2} = ?")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.answer:
                self.score += 1
                self.score_label.config(text=f"Очки: {self.score}")
                self.generate_question()
            else:
                self.end_game()
        except ValueError:
            self.end_game()

    def end_game(self):
        self.question_label.config(text="Игра окончена!")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.config(state='disabled')
        self.submit_button.config(state='disabled')

        final_score_label = tk.Label(self.root, text=f"Ваш итоговый счет: {self.score}", font=("Arial", 18))
        final_score_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    game = MathQuiz(root)
    root.mainloop()
