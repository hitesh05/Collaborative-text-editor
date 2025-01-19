class GSet:
    """
    Grow Only Set CRDT Implementation.

    Notes:
        A set of elements where elements can only be added and once an element is added, it cannot be removed.
        Merging returns union of the two G-Sets.

    Attributes:
        payload (list): List of elements.
        id (any_type): ID of the class object.
    """

    def __init__(self, id):
        self.payload = []
        self.id = id

    def add(self, elem):
        # add elem to list
        self.payload.append(elem)

        # Sort the payload.
        self.payload.sort()

    def query(self, elem):
        # check if elem in list
        return elem in self.payload

    def compare(self, gs2):
        # compare whether lists are same
        list1 = self.payload
        list2 = gs2.payload
        x = lambda list1, list2: len(list1) == len(list2) and all(x == y for x, y in zip(list1, list2))
        return x
        
    def merge(self, gs2):
        # merge elems in gs2 to og list
        for elem in gs2.payload:
            if elem not in self.payload:
                self.payload.append(elem)

        # Sort the payload.
        self.payload.sort()

    def display(self):
        print(self.payload)

class TwoPSet:
    """
    Two-Phase Set CRDT Implementation.

    Notes:
        A set in which elements can be added as well as removed. It combines two G-Sets namely “add” and “remove” set.
        For adding/removing an element, it is inserted in the “add”/“remove” set.
        An element is a member of the set if it is in the “add” set but not in the “remove” set.
        Query function returns whether the element is a member of the set or not.
        Hence, if an element is removed, query will never return True for that element, so it cannot be re-added.
        Merging involves union of the “add”/“remove” sets.

    Attributes:
        A (list): List of elements added.
        R (list): List of elements removed.
        id (any_type): ID of the class object.
    """

    def __init__(self, id):
        self.A = GSet(id)
        self.R = GSet(id)
        self.id = id

    def add(self, elem):
        # add elem by appending to A set
        self.A.add(elem)

    def remove(self, elem):
        # remove elem by appending to R set
        self.R.add(elem)

    def query(self, elem):
        # check if elem should exist
        return self.A.query(elem) and not self.R.query(elem)

    def compare(self, tps2):
        # comapre A and R sets passed
        return self.A.compare(tps2.A) and self.R.compare(tps2.R)

    def merge(self, tps2):
        # merge the A and R sets passed with og
        self.A.merge(tps2.A)
        self.R.merge(tps2.R)

    def display(self):
        # display A and R
        print("A: ", end="")
        self.A.display()
        print("R: ", end="")
        self.R.display()
