class CheckId:
    def __init__(self, id_, list_, label_):
        self.id_ = id_
        self.list_ = list_
        self.label_ = label_

    def check_id(self):
        """Function to check ID"""
        for x in self.list_:
            if x[self.label_] == self.id_:
                return x
            else:
                return False
