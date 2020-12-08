import pickle


class FileHandler:

    def save(self, data):
        with open('savefile.pickle', 'wb') as fout:
            pickle.dump(data, fout)

    def load(self):
        with open('savefile.pickle', 'rb') as fin:
            data = pickle.load(fin)

        return data
