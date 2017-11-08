class Node:
    def __init__(self, id):
        self.id = id
    def type(self):
        return 'node'

class User(Node):
    def __init__(self, id):
        Node.__init__(self, id)
    def type(self):
        return 'user'

class Artist(Node):
    def __init__(self, id, name):
        Node.__init__(self, id)
        self.name = name
    def type(self):
        return 'artist'

class Song(Node):
    def __init__(self, id, title):
        Node.__init__(self, id)
        self.title = title
    def type(self):
        return 'song'

def subtractList(listA, listB):
    return [item for item in listA if item not in listB]

def recommend(graph, user):
    queue = [user]
    visit = []
    songs = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visit:
            visit.append(vertex)
            lst = graph[vertex]
            lst = [x for (x,y) in lst]
            queue.extend(subtractList(lst,visit))
            if vertex.type() == 'song':
                songs.append(vertex)
    print(songs)
    return songs
