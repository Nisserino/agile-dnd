import pickle


class FileHandler:
    '''Handles pickling and saving and loading files'''

    def save(self, data):
        '''Pickles data and saves it to a file'''
        with open('savefile.pickle', 'wb') as fout:
            pickle.dump(data, fout)

    def load(self):
        '''Load data from a file and depickle it. Returns a dict'''
        try:
            with open('savefile.pickle', 'rb') as fin:
                data = pickle.load(fin)
        except Exception:
            data = {}

        return data


class DataHandler:
    '''Handles character data'''

    def __init__(self):
        self.file_handler = FileHandler()
        self.character_data = self.file_handler.load()

    def update(self, data: tuple):
        '''Update the character collection with a
        tuple of username and hero instance'''
        self.character_data[data[0]] = data[1]

    def get_names(self) -> list:
        '''Returns a list of all the used usernames'''
        name_list = []
        for c in self.character_data:
            name_list.append(c)

        return name_list

    def load_character(self, name: str):
        '''Load a character'''
        return self.character_data[name]
