class brick:
    id: int
    cubes: set
    supporting: bool

    def __init__(self, id, cubes, supporting) -> None:
        self.id = id
        self.cubes = cubes 
        self.supporting = supporting 

def tup_add(tuple1, tuple2):
    return tuple(x + y for x, y in zip(tuple1, tuple2))

bricks = {}
i = 0
for line in open('test.txt', 'r').readlines():
    line = line.strip()
    if not line: break
    b1, b2 = line.split('~')
    x1,y1,z1 = [int(_) for _ in b1.split(',')]
    x2,y2,z2 = [int(_) for _ in b2.split(',')]
    cubes = set()
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                cubes.add((x,y,z))
    bricks[i] = brick(i, cubes, False)
    i += 1

decr = (0,0,-1)

for k, v in bricks.items():
    for cube in v.cubes:
        print(cube)


for k, v in bricks.items():
    old = v
    updated = set()
    for cube in v.cubes:
        updated.add(tup_add(cube, decr))
        print(updated)
    bricks[k] = brick(v.id, updated, v.supporting)
    

print('after')
for k, v in bricks.items():
    for cube in v.cubes:
        print(cube)

