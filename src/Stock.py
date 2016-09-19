class Stock:
    def __init__(self):
        self.name = ""
        self.dataset_code = ""
        self.database_code = ""

    def code(self):
        return self.database_code + "/" + self.dataset_code

    def __str__(self):
        return self.code() + "\t" + self.name.partition("(")[0]
