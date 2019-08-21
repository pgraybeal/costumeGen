import osrsbox
from jsonExtract import importPickle, statsLookup


coordinates = {}  # dictionary containing the image coordinates (on the equip tab) of each type of item
image = 0
# IMPORTANT: before this code, you would create variables 'stats' and 'itemSlots', and then import the pickle files
slot = 0
pp = pprint.PrettyPrinter(indent=4)


class Equipment:
    def __init__(
        self,
        image,
        twoHand=None,
        helmet=None,
        amulet=None,
        ring=None,
        body=None,
        legs=None,
        gloves=None,
        boots=None,
        cape=None,
        ammo=None,
        weapon=None,
        shield=None
    ):
        self.image = 'get from osrsdb'  # the equipment tab background
        self.twoHand = twoHand
        self.helmet = helmet
        self.amulet = amulet
        self.ring = ring
        self.body = body
        self.legs = legs
        self.gloves = gloves
        self.boots = boots
        self.cape = cape
        self.ammo = ammo
        self.weapon = weapon
        self.shield = shield

        self.stats = importPickle('stats.pickle')
        self.itemSlots = importPickle('itemSlots.pickle')
        self.slot = 0

        self.equippedItems = {'2h': self.twoHand,  # this Dict will be handy for the equip and statLookup functions
                              'helmet': self.helmet,
                              'amulet': self.amulet,
                              'ring': self.ring,
                              'body': self.body,
                              'legs': self.legs,
                              'gloves': self.gloves,
                              'boots': self.boots,
                              'cape': self.cape,
                              'ammo': self.ammo,
                              'weapon': self.weapon,
                              'shield': self.shield,
                              }

    def equip(self, itemName):
        self.slot = self.itemSlots[itemName.lower()]  # Getting a key error here??? How??
        #image = item.get_image()

        # based on what the slot is, replace the current item with that item
        # then, using coordinates, put the item on the equipment image

        if self.equippedItems[self.slot] == None:
            self.equippedItems[self.slot] = itemName.lower()

        elif self.equippedItems[self.itemSlots[itemName.lower()]] != None:
            self.equippedItems[self.itemSlots[itemName.lower()]] = itemName.lower()
            getAllStats()
            # IMPORTANT: this will replace anything equipped, but if we replace an equipped item, we need to rerun statsLookup

    def getAllStats(self, equippedDict):        # sum of stats of all items
        total = 0
        for itemType, itemName in equippedDict.items():
            statsLookup(itemName.lower())
         # use for loop to run statsLookup on all items, return total
        return total

    def reset(self):
        self.helmet = None
        self.amulet = None
        self.ring = None
        self.body = None
        self.legs = None
        self.gloves = None
        self.boots = None
        self.cape = None
        self.ammo = None
        self.weapon = None
        self.shield = None
        image = 'get from osrsdb'
        self.image = image
        # get image from osrsdb using self.id
        raise NotImplementedError

    def printEquipped(self):
        for k, v in self.equippedItems.items():
            print(f'{k}: {v}')


def main():
    instance = Equipment(image)
    instance.equip('maple longbow')
    instance.printEquipped()


if __name__ == "__main__":
    main()
