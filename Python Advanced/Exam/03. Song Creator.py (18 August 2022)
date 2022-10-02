def add_songs(*args):
    songs = {}
    for i in args:
        if i[0] not in songs:
            songs[i[0]] = []
        songs[i[0]].extend(i[1])
    result = []
    for song_title, song_lyrics in songs.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)
    return "\n".join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
