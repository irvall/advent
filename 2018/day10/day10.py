from collections import deque
from dataclasses import dataclass
import sys, re

@dataclass
class Rocket:
    position: tuple[int,int]
    velocity: tuple[int,int]
    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
    

use_test = len(sys.argv) > 1
file_to_read = 'mini.txt' if use_test else 'input.txt'
lines = [line.rstrip() for line in open(file_to_read, 'r').readlines()]
rgx = r'position=<(.*)> velocity=<(.*)>'
# position=< 7,  6> velocity=<-1, -1>
n = 22
INF = 99999999999
minx, maxx = INF, -INF
miny, maxy = INF, -INF

def move_all(rockets: list[Rocket]):
    global minx,maxx,miny,maxy
    minx, maxx = INF, -INF
    miny, maxy = INF, -INF
    for r in rockets:
        r.move()
        minx = min(minx, r.position[0])
        miny = min(miny, r.position[1])
        maxx = max(maxx, r.position[0])
        maxy = max(maxy, r.position[1])

def mkgrid(rockets: list[Rocket]):
    G = set()
    for rocket in rockets:
        G.add((rocket.position[0], rocket.position[1]))
    return G
        
rockets = []    

def bfs(graph, start):
    queue = [start]
    visited = set(queue)
    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

for line in lines:
    ms = re.match(rgx, line)
    pos = [int(_) for _ in ms[1].split(',')]
    vel = [int(_) for _ in ms[2].split(',')]
    r = Rocket(pos, vel)
    minx = min(minx, pos[0])
    miny = min(miny, pos[1])
    maxx = max(maxx, pos[0])
    maxy = max(maxy, pos[1])
    rockets.append(r)

def pp(G):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) in G:
                print(f'{"#": >3}', end='')
            else:
                print(f'{".": >3}', end='')
        print()
 
clusters = INF       
G = mkgrid(rockets)
s = 1
while (maxy - miny) > 9:
    move_all(rockets)
    s += 1
G = mkgrid(rockets)
pp(G)
print('secs', s)



#print(neighbours(G, )) 
# while clusters > 10:
#     input()
#     move_all(rockets) 
#     G = mkgrid(rockets)
#     clusters = cluster_count(rockets, G)
#     pp(G)
# pp(G) 


    
    
    
    

