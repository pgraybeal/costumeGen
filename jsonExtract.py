#! python3
# import json files for items and dl the pertinent info

import json
import pickle

from osrsbox import items_api
slotJsons = {'2h': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-2h.json',
             'ammo': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-ammo.json',
             'body': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-body.json',
             'cape': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-cape.json',
             'feet': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-feet.json',
             'hands': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-hands.json',
             'head': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-head.json',
             'legs': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-legs.json',
             'neck': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-neck.json',
             'ring': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-ring.json',
             'shield': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-shield.json',
             'weapon': 'https://www.osrsbox.com/osrsbox-db/items-json-slot/items-weapon.json'}
items = []
stats = {}
itemSlots = {}


def id_to_name():
    idToName = {}

    for item in items_api.load():
        id_to_name[item.id] = item.name
    return idToName


def getSlotType(statsDict):
    for slotType in statsDict:
        for item in statsDict[slotType]:
            itemSlots.setdefault(item, statsDict[slotType][item]['slot'])


def extractStats(jsonDict):
    for slotType, jsonUrl in jsonDict.items():
        try:
            from urllib.request import urlopen
        except ImportError:
            from urllib2 import urlopen
        response = urlopen(jsonUrl)
        rawData = response.read().decode("utf-8")
        data = json.loads(rawData)
        stats.setdefault(slotType, {})

        for k, v in data.items():
            for k1, v1 in v.items():
                if k1 == "name":
                    if v1 not in items:
                        items.append(v1.lower())
                if k1 == "equipment":
                    stats[slotType].setdefault(v["name"].lower(), v1)


def importPickle(directory):
    with open(directory, 'rb') as handle:
        stats = pickle.load(handle)
    return stats


def statsLookup(itemName, statsDict, itemSlotsDict):  # itemSlotsDict is my dict with just itemName:itemType
    if itemName == None:
        return {'attack_stab': 0, 'attack_slash': 0, 'attack_crush': 0, 'attack_magic': 0, 'attack_ranged': 0, 'defence_stab': 0, 'defence_slash': 0, 'defence_crush': 0, 'defence_magic': 0, 'defence_ranged': 0, 'melee_strength': 0, 'ranged_strength': 0, 'magic_damage': 0, 'prayer': 0, 'slot': None, 'requirements': ''}
    else:
        itemType = itemSlotsDict[itemName.lower()]
        return statsDict[itemType][itemName.lower()]


def main():
    stats = importPickle('stats.pickle')
    itemSlots = importPickle('itemSlots.pickle')
    statsLookup('Maple longbow', stats, itemSlots)
    #print(itemSlots['Maple longbow'.lower()])

    # No need to run the below anymore, can just import locally (NOTE TO SIYANG: you can't use directories with importing pickles, save locally)
    # getSlotType(stats)
    # extractStats(slotJsons)


if __name__ == "__main__":
    main()
