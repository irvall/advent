import sys

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
line = open(file_to_read, 'r').read()

LP = None
LD = None

class MemoryBlock:
    def __init__(self, size, value=None):
        self.size = size
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        has_next = 'None' if not self.next else '*'
        return f'MBlock[size={self.size}, value={self.value}, next={has_next}]'
    
    def __repr__(self):
        return self.__str__()

class GarbageCollector:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        blocks = self.as_list()
        header = '----- GC TRACE -----\n'
        stringified = [f'[{'FREE' if block.value == None else f'value={block.value}'}, size={block.size}]' for block in blocks]
        return header + ' -> '.join(stringified)
    
    def simple_str(self):
        tmp = self.head
        res = ''
        while tmp:
            is_data = tmp.value != None
            res += (str(tmp.value) if is_data else '.')*tmp.size
            tmp = tmp.next
        return res 
    
    def last_data(self):
        tmp = self.tail
        while tmp.value == None:
            tmp = tmp.prev
        return tmp

    def as_list(self):
        res = []
        root = self.head
        while root:
            res.append(root)
            root = root.next
        return res

    def add_block(self, size, value=None):
        block = MemoryBlock(size, value)
        block.prev = self.tail
        if not self.tail:
            self.head = block
        else:
            self.tail.next = block
        self.tail = block
    
    def next_free(self):
        tmp = self.head
        while tmp and tmp.value != None:
            tmp = tmp.next
        return tmp

    def free_size(self):
        res = 0
        tmp = self.next_free()
        while tmp:
            if tmp.value == None:
                res += tmp.size
            tmp = tmp.next
        return res
    
    def 
    


    def write(self):
        free_block = self.next_free()
        last_data = self.last_data()
        if not (free_block or last_data):
            raise BufferError('Free block or data was not available')
        print(free_block, last_data)
        diff = free_block.size - last_data.size
        free_block.value = last_data.value
        free_block.size = last_data.size
        last_data.value = None
        if diff > 0:
            ptr = free_block.next
            mem = MemoryBlock(diff)
            mem.next = ptr
            free_block.next = mem
        

        
    


    
gc = GarbageCollector()
is_free = False
ID = 0
for c in line.strip():
    v = ID
    if is_free:
        gc.add_block(int(c))
    else:
        gc.add_block(int(c), v)
    is_free = not is_free
    if not is_free:
        ID += 1

for _ in range(3):
    print(gc.simple_str())
    gc.write()