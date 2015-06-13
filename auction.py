import json
import random
import pymongo as mg

def GetAll():
    """
    image, price, name
    """
    coll = mg.MongoClient()['migros']['lebensmittel']
    item_num = 291
    hasImage = coll.find({'info.image.medium':{'$exists':True}})
    _table = list()
    for iter in xrange(item_num):
        item = hasImage.next()
        # item.update({'price': round(random.uniform(2, 50), 2)})
        info = dict()
        info["id"] = item["id"]
        info["image"] = item['info']['image']
        info['price'] = item['health']
        info['description'] = "This is a real description...."
        info['name'] = item['name']
        _table.append(info)
    return _table

def GetByID(id):
    col = mg.MongoClient()['migros']['lebensmittel']
    cursor = col.find({'id': int(id)})
    for item in cursor:
        return item

def PlaceABid(id, price):
    col = mg.MongoClient()['migros']['lebensmittel']
    cursor = col.update({"id": int(id)}, {'$set': {'health': price}}, False)
    print cursor
