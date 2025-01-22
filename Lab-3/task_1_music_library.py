def make_album(artist_name, album_title, num_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_songs is not None:
        album['songs'] = num_songs
    return album

albums = []
for i in range(3):
    print(f"Enter details for album {i + 1}:")
    artist = input("Artist name: ")
    title = input("Album title: ")
    songs = input("Number of songs (press Enter to skip): ")
    if songs:
        albums.append(make_album(artist, title, int(songs)))
    else:
        albums.append(make_album(artist, title))

for i, album in enumerate(albums, 1):
    print(f"Album {i}: {album}")
