import osrsdb

class Item:
    def __init__(
        self,
        id,
        slot,
        metadata
    ):
        self.id = id
        self.slot = slot
        self.metadata = metadata #all other fields - bonuses, level reqs, GE price, quest item. i'm picturing this as a dictionary, but could be in any format

    def get_stats(self):
        return(self.metadata['bonuses']) #this assumes metadata is a dictionary with lists as values / nested dict


    def get_image(self):
        #get image from osrsdb using self.id
        raise NotImplementedError

#implement NullItem
