class PairTrader:
    def __init__(self):
        self.pairs = []

    def learn_pairs(self, history):
        self.pairs.append((history.columns[0], history.columns[1]))
        self.pairs.append((history.columns[2], history.columns[3]))
