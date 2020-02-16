for _ in range(int(input())):
    num_songs = int(input())
    songs_list = []
    for i in range(num_songs):
        songs_list.append(tuple(map(int, input().split())))
    songs_list.sort(key = lambda x: x[1])
    played_list = [False]*num_songs
    previously_palyed = {}
    sweetness = 0
    for i in range(len(songs_list)):
        song = songs_list[i]
        if song[0] not in previously_palyed:
            previously_palyed[song[0]] = True
            sweetness += song[1] * len(previously_palyed)
            played_list[i] = True
    for i in range(len(songs_list)):
        song = songs_list[i]
        if not played_list[i]:
            sweetness += song[1] * len(previously_palyed)
    print(sweetness)
