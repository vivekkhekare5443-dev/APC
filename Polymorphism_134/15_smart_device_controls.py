"""
Polymorphism - Program 15:
Create a base class SmartDevice with methods turn_on() and turn_off().
Derive Light, Fan, AC, and TV.
Override the methods according to each device.
"""

class SmartDevice:
    def __init__(self, room, device_id):
        self.room = room
        self.device_id = device_id
        self.is_powered = False

    def turn_on(self):
        self.is_powered = True
        print(f"{self.__class__.__name__} ({self.device_id}) turned on.")

    def turn_off(self):
        self.is_powered = False
        print(f"{self.__class__.__name__} ({self.device_id}) turned off.")


class Light(SmartDevice):
    def __init__(self, room, device_id, brightness_percent=100, color="Warm White"):
        super().__init__(room, device_id)
        self.brightness_percent = brightness_percent
        self.color = color

    def turn_on(self):
        self.is_powered = True
        print(f"[Smart Light] {self.room}: Illuminated with {self.color} color at {self.brightness_percent}% brightness.")

    def turn_off(self):
        self.is_powered = False
        print(f"[Smart Light] {self.room}: Dimmed and turned off.")


class Fan(SmartDevice):
    def __init__(self, room, device_id, speed_level=3):
        super().__init__(room, device_id)
        self.speed_level = speed_level

    def turn_on(self):
        self.is_powered = True
        print(f"[Smart Fan] {self.room}: BLDC motor started rotating at speed level {self.speed_level}.")

    def turn_off(self):
        self.is_powered = False
        print(f"[Smart Fan] {self.room}: Decelerating to complete stop.")


class AC(SmartDevice):
    def __init__(self, room, device_id, target_temp=24):
        super().__init__(room, device_id)
        self.target_temp = target_temp

    def turn_on(self):
        self.is_powered = True
        print(f"[Smart AC] {self.room}: Compressor initiated in Cool Mode, target temperature set to {self.target_temp}°C.")

    def turn_off(self):
        self.is_powered = False
        print(f"[Smart AC] {self.room}: Compressor powered down, louvers closed.")


class TV(SmartDevice):
    def __init__(self, room, device_id, current_app="Netflix"):
        super().__init__(room, device_id)
        self.current_app = current_app

    def turn_on(self):
        self.is_powered = True
        print(f"[Smart TV] {self.room}: OLED display turned on. Launching '{self.current_app}' on HDMI-1.")

    def turn_off(self):
        self.is_powered = False
        print(f"[Smart TV] {self.room}: Entering low-power standby mode.")


if __name__ == "__main__":
    home_automation = [
        Light("Living Room", "LGT-01"),
        Fan("Master Bedroom", "FAN-02"),
        AC("Living Room", "AC-01"),
        TV("Home Theater", "TV-01")
    ]

    print("=== IoT Smart Home Automation Hub: Evening Routine (Turn On All) ===")
    for dev in home_automation:
        dev.turn_on()

    print("\n=== IoT Smart Home Automation Hub: Bedtime Routine (Turn Off All) ===")
    for dev in home_automation:
        dev.turn_off()
