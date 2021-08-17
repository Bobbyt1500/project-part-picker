class Project:
    def __init__(self, id, name, parts = []):
        self.id = id
        self.name = name
        self.parts = parts
    
    def get_json(self):
        parts_list = []
        for part in self.parts:
            parts_list.append(part.get_json())

        return {
            "_id" : self.id,
            "name" : self.name,
            "parts" : parts_list
        }
    
    def get_price(self):
        price = 0
        for part in self.parts:
            price += int(part.price)

        return price
    
    @classmethod
    def from_json(cls, data):
        parts = []
        for part_data in data["parts"]:
            parts.append(Part(part_data["_id"], part_data["name"], part_data["link"], part_data["price"]))

        return cls(data["_id"], data["name"], parts)

class Part:
    def __init__(self, id, name, link, price):
        self.id = id
        self.name = name
        self.link = link
        self.price = price
    
    def get_json(self):
        return {
            "_id" : self.id,
            "name" : self.name,
            "link" : self.link,
            "price" : self.price
        }

