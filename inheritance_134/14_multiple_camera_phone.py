"""
Inheritance - Program 14 (Multiple Inheritance):
Create classes Camera and Phone. The Camera class should provide methods for
taking photographs, while Phone should provide methods for making calls.
Create a Smartphone class inheriting from both.
"""

class Camera:
    def __init__(self, megapixels, optical_zoom):
        self.megapixels = megapixels
        self.optical_zoom = optical_zoom

    def take_photo(self, subject):
        print(f"[Camera] Captured high-resolution photo of '{subject}' ({self.megapixels} MP, {self.optical_zoom}x optical zoom).")

    def record_video(self, resolution="4K"):
        print(f"[Camera] Recording video in {resolution} resolution at 60 FPS.")


class Phone:
    def __init__(self, sim_count, network_type):
        self.sim_count = sim_count
        self.network_type = network_type

    def make_call(self, contact_number):
        print(f"[Phone] Dialing {contact_number} over {self.network_type} network...")

    def send_sms(self, contact_number, message):
        print(f"[Phone] SMS sent to {contact_number}: \"{message}\"")


class Smartphone(Camera, Phone):
    def __init__(self, device_name, os_name, megapixels, optical_zoom, sim_count, network_type):
        Camera.__init__(self, megapixels, optical_zoom)
        Phone.__init__(self, sim_count, network_type)
        self.device_name = device_name
        self.os_name = os_name

    def display_specs(self):
        print(f"=== Smartphone: {self.device_name} ({self.os_name}) ===")
        print(f"Camera Specs : {self.megapixels} MP with {self.optical_zoom}x zoom")
        print(f"Network Type : {self.network_type} (Dual SIM: {self.sim_count == 2})")


if __name__ == "__main__":
    my_phone = Smartphone("Pixel Pro 9", "Android 15", megapixels=50, optical_zoom=5, sim_count=2, network_type="5G")
    my_phone.display_specs()
    print()
    my_phone.make_call("+91-9876543210")
    my_phone.take_photo("Sunset over the Campus")
    my_phone.send_sms("+91-9876543210", "See you at the library!")
