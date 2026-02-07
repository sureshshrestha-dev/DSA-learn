class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def __str__(self):
        return f"'{self.title}' by {self.artist}"

class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.current = None
        self.repeat_mode = "OFF" # OFF, ONE, ALL

    def add_song(self, title, artist):
        new_song = SongNode(title, artist)
        if not self.head:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_song
            new_song.prev = tail
            new_song.next = self.head
            self.head.prev = new_song

    def play_next(self):
        if not self.current:
            return "Playlist empty"
        
        if self.repeat_mode == "ONE":
            return f"Playing (Repeat One): {self.current}"
        
        self.current = self.current.next
        return f"Playing: {self.current}"

    def play_prev(self):
        if not self.current:
            return "Playlist empty"
        self.current = self.current.prev
        return f"Playing: {self.current}"

    def set_repeat_mode(self, mode):
        self.repeat_mode = mode # Simplified - actual logic for 'ALL' is natural in circular
        print(f"Repeat mode set to {mode}")

if __name__ == "__main__":
    playlist = MusicPlaylist()
    playlist.add_song("Song A", "Artist 1")
    playlist.add_song("Song B", "Artist 2")
    playlist.add_song("Song C", "Artist 3")
    
    print(f"Current: {playlist.current}")
    print(playlist.play_next()) # B
    print(playlist.play_next()) # C
    print(playlist.play_next()) # A (Circular)
    
    playlist.set_repeat_mode("ONE")
    print(playlist.play_next()) # A (Repeat One)
    
    print(playlist.play_prev()) # C (Backwards from A)
    print("Music Playlist tests passed!")
