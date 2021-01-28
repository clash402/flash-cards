from tkinter import *
import random


class UI(Tk):
    def __init__(self, data_manager):
        super().__init__()

        self.data_manager = data_manager

        self.BACKGROUND_COLOR = "#B1DDC6"

        self.words_to_learn = self.data_manager.load_data()
        self.current_card = random.choice(self.words_to_learn)
        self.timer = self.after(3000, self._flip_card)

        self.title("Flash Cards")
        self.config(padx=56, pady=56, bg=self.BACKGROUND_COLOR)

        self._draw()
        self._go_to_next_card()

    # DRAW METHODS
    def _draw(self):
        self._draw_canvas()
        self._draw_card_front()
        self._draw_card_back()
        self._draw_wrong_button()
        self._draw_right_button()

    # Canvas
    def _draw_canvas(self):
        self.card_front_img = PhotoImage(file="./images/card_front.png")
        self.card_back_img = PhotoImage(file="./images/card_back.png")

        self.canvas = Canvas(width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0)

        self.card_img = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

        self.canvas.grid(column=0, row=0, columnspan=2)

    # Cards
    def _draw_card_front(self):
        self.canvas.itemconfig(self.card_img, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")

    def _draw_card_back(self):
        self.canvas.itemconfig(self.card_img, image=self.card_back_img)
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")

    # Buttons
    def _draw_wrong_button(self):
        self.wrong_img = PhotoImage(file="./images/wrong.png")
        wrong_button = Button(image=self.wrong_img, command=self._wrong_button_clicked, highlightthickness=0)
        wrong_button.grid(column=0, row=1)

    def _draw_right_button(self):
        self.right_img = PhotoImage(file="./images/right.png")
        right_button = Button(image=self.right_img, command=self._right_button_clicked, highlightthickness=0)
        right_button.grid(column=1, row=1)

    # UPDATE METHODS
    def _update_words_to_learn(self):
        self.words_to_learn.remove(self.current_card)
        self.data_manager.save_data(self.words_to_learn)

    # CARD METHODS
    def _go_to_next_card(self):
        self.current_card = random.choice(self.words_to_learn)
        self._draw_card_front()
        self._countdown()

    def _flip_card(self):
        self._draw_card_back()

    def _countdown(self):
        self.timer = self.after_cancel(self.timer)
        self.timer = self.after(3000, self._flip_card)

    # EVENTS
    def _wrong_button_clicked(self):
        self._go_to_next_card()

    def _right_button_clicked(self):
        self._update_words_to_learn()
        self._go_to_next_card()
