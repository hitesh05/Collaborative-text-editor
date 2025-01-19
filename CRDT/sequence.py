# static methods for sequence crdt
class SeqFunctions:
    @staticmethod
    def add(payload, elem, id):
        # add tuple to list and sort by id
        payload.append((elem, id))
        payload.sort(key=lambda i: i[1])
        return payload

    @staticmethod
    def remove(payload, id):
        # Add the ID of elem to be removed to the list of to_remove elems
        payload.append(id)
        # Sort
        payload.sort()
        return payload

    @staticmethod
    def merge(payload1, payload2):
        # merge the lists: [list to be merged to] + [list to be merged from]
        for i in payload2:
            if i not in payload1:
                payload1.append(i)
        return payload1


    @staticmethod
    def get_seq(payload):
        # return str of elems in list
        seq = ""
        for elem in payload:
            seq += elem
        return seq


class Sequence():
    """
    Sequence CRDT Implementation.

    Notes:
        An ordered set, list or a sequence of elements.

    Attributes:
        elem_list (list): List of elements added.
        id_remv_list (list): List of IDs removed.
        id_seq (list): List of IDs in sequence.
        id_elem_seq (list): List of elements in sequence.
        id (any_type): ID of the class object.
        seqf (SeqFunctions): SeqFunctions object to access the static methods.
    """

    def __init__(self, id):
        self.elem_list = []
        self.id_remv_list = []
        self.id_seq = []
        self.elem_seq = []
        self.id = id
        self.seqf = SeqFunctions()

    def update_seq(self):
        for item in self.elem_list:
            if item[1] not in self.id_remv_list and item[1] not in self.id_seq:
                self.id_seq.append(item[1])
        for id in self.id_remv_list:
            if id in self.id_seq:
                del self.elem_seq[self.id_seq.index(id)]
                self.id_seq.remove(id)
        self.id_seq.sort()
        for id in self.id_seq:
            for item in self.elem_list:
                if item[1] == id:
                    if len(self.elem_seq) > self.id_seq.index(id):
                        if item[0] != self.elem_seq[self.id_seq.index(id)]:
                            self.elem_seq.insert(self.id_seq.index(id), item[0])
                    else:
                        self.elem_seq.append(item[0])

    def add(self, elem, id):
        # elem,id to be added
        self.elem_list = self.seqf.add(self.elem_list, elem, id)
        
        # update the sequence
        self.update_seq()

    def remove(self, id):
        # remove elem by adding id to id_remv_list
        self.id_remv_list = self.seqf.remove(self.id_remv_list, id)

        # update the sequence
        self.update_seq()



    def merge(self, list, func='na'):
        # merge the passed list with original list
        
        # default merge both
        if func == 'na':
            self.elem_list = self.seqf.merge(self.elem_list, list.elem_list)
            self.id_remv_list = self.seqf.merge(self.id_remv_list, list.id_remv_list)
        # only merge elem_list
        elif func == 'elem':
            self.elem_list = self.seqf.merge(self.elem_list, list)
        # only mege id list
        elif func == 'id':
            self.id_remv_list = self.seqf.merge(self.id_remv_list, list)
        self.update_seq()


    def get_seq(self):
        # return seq as str
        return self.seqf.get_seq(self.elem_seq)
