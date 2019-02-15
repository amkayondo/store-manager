from flask import jsonify
class CheckId:
    def __init__(self, id_, list_, label_, name_):
        self.id_ = id_
        self.list_ = list_
        self.label_ = label_
        self.name_ = name_

    def check_id(self):
        """Function to check ID"""
        for x in self.list_:
            if x[self.label_] == self.id_:
                return x
            else:
                return False
    
    def check_name(self):
        """Function to check name"""
        for name in self.list_:
            if name[self.name_] == self.name_:
                return jsonify({
                    "message": name + "already exists"
                })
        else:
            return False
    