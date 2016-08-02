__author__ = '__naresh__'


# Hash Map Implementation with Linear Probing Hash Function

class HashMap(object):
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.slots = [None] * self.size

    def put(self, key, value):
        hashval = key % self.size
        if self.slots[hashval] and self.slots[hashval] == key:
            self.keys[hashval] = value
            return
        while self.slots[hashval] is not None and self.slots[hashval] != key:
            hashval = self.rehash(hashval)

        if self.slots[hashval] is None:
            self.slots[hashval] = key
            self.keys[hashval] = value
            return
        else:
            self.keys[hashval] = value
            return

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def get(self, key):
        hashval = key % self.size
        startval = self.slots[hashval]
        if self.slots[hashval] == key:
            return self.keys[hashval]
        else:
            hashval = self.rehash(hashval)
            while self.slots[hashval] != key and self.slots[hashval] != startval and self.slots[hashval] is not None:
                hashval = self.rehash(hashval)
            if self.slots[hashval] == key:
                return self.keys[hashval]
            else:
                return None

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)


if __name__ == "__main__":
    H = HashMap()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print "Slots", H.slots
    print "Keys", H.keys
    print H[20]
    H[20] = "XUX"
    print H[20]
    print H[84]