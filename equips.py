import osrsdb
from item import Item, NullItem

coordinates = {} #dictionary containing the image coordinates (on the equip tab) of each type of item


class EquipmentView:
    def __init__(
        self,
        image,
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
        self.image = 'get from osrsdb' #the equipment tab background
        self.helmet=helmet
        self.amulet=amulet
        self.ring=ring
        self.body=body
        self.legs=legs
        self.gloves=gloves
        self.boots=boots
        self.cape=cape
        self.ammo=ammo
        self.weapon=weapon
        self.shield=shield

    def equip(self, item):
        slot = item.slot
        image = item.get_image()
        #based on what the slot is, replace the current item with that item
        #then, using coordinates, put the item on the equipment image


    def get_stats(self):
        total = 0
        #sum of stats of all items
        return total


    def reset(self):
        self.helmet=None
        self.amulet=None
        self.ring=None
        self.body=None
        self.legs=None
        self.gloves=None
        self.boots=None
        self.cape=None
        self.ammo=None
        self.weapon=None
        self.shield=None
        image = 'get from osrsdb'
        self.image = image
        #get image from osrsdb using self.id
        raise NotImplementedError
