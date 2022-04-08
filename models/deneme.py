from factory.database import Database


class Deneme(object):
    def __init__(self):
        self.db = Database()

        self.collection_name = 'deneme'

        self.fields = {
            "title": "string",
            "body": "string",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["title", "body"]

        self.create_optional_fields = []

        self.update_required_fields = ["title", "body"]

        self.update_optional_fields = []

    def create(self, deneme):
        res = self.db.insert(deneme, self.collection_name)
        return "Inserted Id " + res

    def find(self, deneme):
        return self.db.find(deneme, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, deneme):
        return self.db.update(id, deneme,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)
