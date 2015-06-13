import json
import random
import pymongo as mg

def GetAll():
    """
    Get all the "image, price, name, ..."
    """
    coll = mg.MongoClient()['migros']['lebensmittel']
    hasImage = coll.find({'info.image.medium':{'$exists':True}})
    _table = list()
    for iter in xrange(hasImage.count()):
        item = hasImage.next()
        info = dict()
        info["id"] = item["id"]
        info["image"] = item['info']['image']
        info['price'] = item['health']
        info['description'] = "This is a real description...."
        info['name'] = item['name']
        _table.append(info)
    return _table

def GetByID(id):
    """
    Get the product by its ID
    """
    col = mg.MongoClient()['migros']['lebensmittel']
    cursor = col.find({'id': int(id)})
    for item in cursor:
        return item

def PlaceABid(id, price):
    """
    Place a bid on the product
    """
    col = mg.MongoClient()['migros']['lebensmittel']
    col.update({"id": int(id)}, {'$set': {'health': price}}, False)
