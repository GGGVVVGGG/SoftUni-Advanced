def add_songs(*args):
    songs = {}
    result_string = f''
    for this in args:
        song, lyrics = this[0], this[1]
        if song not in songs:
            songs[song] = lyrics
        else:
            songs[song] += lyrics

    for s, l in songs.items():
        result_string += f"- {s}\n"
        for line in l:
            result_string += f"{line}\n"

    return result_string