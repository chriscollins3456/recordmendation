class Node:
    def __init__(self, id, name):
        self.id = id
        self.children = []
        self.name = name
    def type(self):
        return 'node'
    def add_child(self, node, weight):
        self.children.append((node, weight))
    def get_weight(self, node, visited = None, weight = None):
        if self == node:
            return weight
        if visited is None:
            visited = []
        if weight is None:
            weight = 0.0
        if self.children == []:
            return False
        weights = []
        for (child, dist) in self.children:
            if child not in visited:
                visited.append(child)
                w = child.get_weight(node, visited, weight + dist)
                if w != None:
                    weights.append(w)
        if weights == []:
            return(10000)
        else:
            for visit in visited:
                print(visit.name)
            print(weights)
            return(min(weights))
    def rank_songs(self, songs):
        song_weights = [(song, self.get_weight(song)) for song in songs]
        ranked = []
        while song_weights:
            ranked.append(min(song_weights, key = lambda t: t[1]))
            song_weights.remove(min(song_weights, key = lambda t: t[1]))
        return(ranked)

class User(Node):
    def type(self):
        return 'user'

class Artist(Node):
    def type(self):
        return 'artist'

class Song(Node):
    def type(self):
        return 'song'


def subtractList(listA, listB):
    return [item for item in listA if item not in listB]


def recommend(user):
    queue = [user]
    visit = []
    songs = []
    likes = user.children
    likes = [x for (x,y) in likes]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visit:
            visit.append(vertex)
            connections = vertex.children
            connections = [x for (x,y) in connections]
            queue.extend(subtractList(connections,visit))
            if vertex.type() == 'song' and vertex not in likes:
                songs.append(vertex)
    return user.rank_songs(songs)
