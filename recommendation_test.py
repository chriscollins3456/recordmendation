from recommendation import User, Artist, Song, recommend

u1 = User(1)
u2 = User(2)
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

#assert that everything in the list returned is a Song
for song in recommend(graph, u1):
    #assert song.type == 'song'
    print(song.title)

#assert that it is in the order of the scores
#assert recommend(graph, u1) == [s2, s5, s4]
#assert recommend(graph, u2) == [s4]
