import pandas


class DataManager:
    def __init__(self):
        self.PATH_WORDS = "./data/french_words.csv"
        self.PATH_WORDS_TO_LEARN = "./data/words_to_learn.csv"

    def load_data(self):
        try:
            data = pandas.read_csv(self.PATH_WORDS_TO_LEARN)
        except FileNotFoundError:
            data = pandas.read_csv(self.PATH_WORDS)

        return data.to_dict(orient="records")

    def save_data(self, words_to_learn):
        data = pandas.DataFrame(words_to_learn)
        data.to_csv(self.PATH_WORDS_TO_LEARN, index=False)
