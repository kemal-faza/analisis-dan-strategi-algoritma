# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2

n, t = map(int, input().split())
playlist = []
fokusBoost = 0

for i in range(n):
    newSong = list(map(int, input().split()))
    if newSong[0] < 5:
        playlist.append(newSong)


def explorePlaylist(sisaWaktu, previousSong, totalFokus):
    global fokusBoost
    if fokusBoost <= totalFokus:
        fokusBoost = totalFokus
    for song in playlist:
        if song != previousSong and song[0] <= sisaWaktu:
            explorePlaylist(sisaWaktu - song[0], song, totalFokus + song[1])


explorePlaylist(t, -1, 0)

print(fokusBoost)


# def explorePlaylist(index, totalTime, totalFokus):
#     global fokusBoost

#     if totalTime > t:
#         return

#     if totalTime <= t and totalFokus > fokusBoost:
#         fokusBoost = totalFokus
#         return

#     if index < 0 or index >= len(playlist):
#         return

#     explorePlaylist(
#         index - 1, totalTime + playlist[index][0], totalFokus + playlist[index][1]
#     )
#     explorePlaylist(
#         index + 1, totalTime + playlist[index][0], totalFokus + playlist[index][1]
#     )

# explorePlaylist(0, 0, 0)


# indexSong = -1
# while t > 0:
#     currentSong = [0, 0, 0]
#     for song in playlist:
#         print(song[0], indexSong)
#         if indexSong != song[0] and song[1] <= t and song[2] > currentSong[2]:
#             indexSong = song[0]
#             currentSong = song
#     fokusBoost += currentSong[2]
#     # print(currentSong)
#     t -= currentSong[1]
