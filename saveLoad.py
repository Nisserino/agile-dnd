import pickle


class FileHandler:

    def save(self, data):
        with open('savefile.pickle', 'wb') as fout:
            pickle.dump(data, fout)

    def load(self):
        try:
            with open('savefile.pickle', 'rb') as fin:
                data = pickle.load(fin)
        except Exception:
            data = {}

        return data


class DataHandler:
    def __init__(self):
        self.character_data = {}

    def update(self, data: tuple):
        self.character_data[data[0]] = data[1]

    def get_names(self) -> list:
        name_list = []
        for c in self.character_data:
            name_list.append(c)

        return name_list

    def load_character(self, name: str):
        return self.character_data[name]
