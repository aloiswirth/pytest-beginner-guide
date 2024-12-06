from bicycle.wheel import Wheel
from bicycle.observer import Observer


class Gear:
    def __init__(
        self, chainring: float, cog: int, wheel: Wheel, observer: Observer = None
    ):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
        self.observer = observer

    def gear_inches(self) -> float:
        """
        Query to calculate the gear inches
        """
        return round(self.__ratio() * self.wheel.diameter(), 2)

    def __ratio(self) -> float:
        """
        Internal method to calculate the ratio
        """
        return round(self.chainring / self.cog, 2)

    def set_cog(self, new_cog_value: int):
        """
        Command to set the cog value
        """
        self.cog = new_cog_value  # Set the cog value for future calculations
        self.changed()

    def changed(self):
        """
        Send a message to the observer that the cog value has changed
        """
        if self.observer:
            self.observer.changed(
                self.chainring, self.cog
            )  # Sends a message to the observer that the cog value has changed, message MUST be sent
            pass