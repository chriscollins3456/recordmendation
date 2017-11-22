from recommendation import Node, User, Artist, Song, recommend

u1 = User(1, 'user1')
u2 = User(2, 'user2')
a1 = Artist(1, 'artist1')
a2 = Artist(2, 'artist2')
s1 = Song(1, 'song1')
s2 = Song(2, 'song2')
s3 = Song(3, 'song3')
s4 = Song(4, 'song4')
s5 = Song(5, 'song5')

graph = {
    u1 : [(s1, 0.2), (a1, 0.4), (u2, 0.9)],
    u2 : [(s5, 0.2), (a2, 0.4)],
    a1 : [(s1, 0.05), (s2, 0.05), (s3, 0.05), (u1, 0.4)],
    a2 : [(s4, 0.05), (s5, 0.05), (u2, 0.4)],
    s1 : [(a1, 0.05), (u1, 0.2)],
    s2 : [(a1, 0.05)],
    s3 : [(a1, 0.05)],
    s4 : [(a2, 0.05)],
    s5 : [(a2, 0.05), (u2, 0.2)]
}

g = Node(0, "graph")
g.add_child(u1, 0)
u1.add_child(s1, 0.2)
u1.add_child(a1, 0.4)
u1.add_child(u2, 0.9)
u2.add_child(s5, 0.2)
u2.add_child(a2, 0.4)
a1.add_child(s1, 0.05)
a1.add_child(s2, 0.05)
a1.add_child(s3, 0.05)
a1.add_child(u1, 0.4)
a2.add_child(s4, 0.05)
a2.add_child(s5, 0.05)
a2.add_child(u2, 0.4)
s1.add_child(a1, 0.05)
s1.add_child(u1, 0.2)
s2.add_child(a1, 0.05)
s3.add_child(a1, 0.05)
s4.add_child(a2, 0.05)
s5.add_child(a2, 0.05)
s5.add_child(u2, 0.2)

print(u1.get_weight(u2))

#for song in u1.rank_songs([s2, s3, s4, s5]):
    #print(song[0].name)

#for song in recommend(u1):
    #print(song[0].name, song[1])

#assert that everything in the list returned is a Song
#for song in recommend(u1):
    #assert song[0].type() == 'song'
#    print(song[0].name, song[1])

#assert that it is in the order of the scores
#assert recommend(u1) == [(s2, 0.3), (s3, 0.3), (s5, 1.75), (s4, 1.85)]
#assert recommend(graph, u2) == [s4]

#assert that weight is greater than 0
#assert recommend(u1)[0][1] > 0
#assert recommend(u2)[0][1] > 0
