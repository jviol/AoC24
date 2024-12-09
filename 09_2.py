
class Slot:
    def __init__(self, c):
        self.data = []
        self.free_space = int(c)

    def __repr__(self):
        return f"(data:{self.data}, free_space:{self.free_space}"


with open('input/09.txt') as f:
    s = f.read().strip()
    files = [(id, int(file_size)) for id, file_size in enumerate(s[0::2])]
    empty_spaces = [Slot(c) for c in s[1::2]]


moved = set()
for file_id, file_size in files[::-1]:
    print("\r", len(files)-file_id, "/", len(files), end='', flush=True)
    for slot_id, slot in enumerate(empty_spaces):
        if slot_id >= file_id:  # only move files to the left
            break
        if slot.free_space >= file_size:
            slot.data += [file_id] * file_size
            slot.free_space -= file_size
            moved.add(file_id)
            break


layout = []
for id, file_size in files:
    layout += [id if id not in moved else 0]*file_size
    if id < len(empty_spaces):
        slot = empty_spaces[id]
        layout += slot.data + [0]*slot.free_space

print("\nPart 2:", sum(i*x for i,x in enumerate(layout)))
