import json
import random
import pymongo as mg

coll = mg.MongoClient()['migros']['lebensmittel']
item_num = 292

def GetAll():
    """
    image, price, name
    """
    hasImage = coll.find({'info.image.medium':{'$exists':True}})
    _table = list()
    for iter in xrange(item_num):
        item = hasImage.next()
        item.update({'price': round(random.uniform(2, 50), 2)})
        _table.append(item['id'])
    return _table
def GetByID(id):
    return coll.find_one({'id':id})

# if __name__ == "__main__":
