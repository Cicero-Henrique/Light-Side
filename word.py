class Word:

    def __init__(self, array, camel):
        self.cases =  {
            "lower": array[0],
            "title": array[2],
            "camel": camel
        }
