"""
Polymorphism - Program 14:
Create a base class Media with a method play().
Derive Audio, Video, and Podcast.
Override play() according to the media type.
"""

class Media:
    def __init__(self, title, duration_minutes):
        self.title = title
        self.duration_minutes = duration_minutes

    def play(self):
        print(f"Playing media stream: {self.title}")


class Audio(Media):
    def __init__(self, title, duration_minutes, artist, bitrate_kbps=320):
        super().__init__(title, duration_minutes)
        self.artist = artist
        self.bitrate_kbps = bitrate_kbps

    def play(self):
        print(f"[Audio Player] Playing track: '{self.title}' by {self.artist}")
        print(f"  Duration: {self.duration_minutes} mins | High-Fidelity Audio ({self.bitrate_kbps} kbps FLAC/MP3)")


class Video(Media):
    def __init__(self, title, duration_minutes, resolution="4K UHD", frame_rate=60):
        super().__init__(title, duration_minutes)
        self.resolution = resolution
        self.frame_rate = frame_rate

    def play(self):
        print(f"[Video Player] Streaming video: '{self.title}'")
        print(f"  Duration: {self.duration_minutes} mins | Resolution: {self.resolution} @ {self.frame_rate} FPS with HDR10")


class Podcast(Media):
    def __init__(self, title, duration_minutes, host_name, episode_number):
        super().__init__(title, duration_minutes)
        self.host_name = host_name
        self.episode_number = episode_number

    def play(self):
        print(f"[Podcast Player] Streaming Episode #{self.episode_number}: '{self.title}'")
        print(f"  Hosted by: {self.host_name} | Duration: {self.duration_minutes} mins | Chapter markers active")


if __name__ == "__main__":
    playlist = [
        Audio("Bohemian Rhapsody", 5.9, "Queen"),
        Video("Interstellar Space Walk", 14.2, resolution="4K Dolby Vision"),
        Podcast("The AI Revolution", 48.0, "Lex Fridman", episode_number=410)
    ]

    print("=== Universal Media Center Playback (Polymorphism) ===")
    for item in playlist:
        item.play()
        print()
