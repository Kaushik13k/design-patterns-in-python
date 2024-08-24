from abc import ABC, abstractmethod


# Observer interface that all observers must implement
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Subject interface that will be implemented by the WeatherStation
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Concrete observer that displays weather data
class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(
            f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity"
        )


# Another observer, for example, a statistics display
class StatisticsDisplay(Observer):
    def __init__(self):
        self.max_temp = float("-inf")
        self.min_temp = float("inf")
        self.temp_sum = 0.0
        self.num_readings = 0

    def update(self, temperature, humidity, pressure):
        self.temp_sum += temperature
        self.num_readings += 1

        if temperature > self.max_temp:
            self.max_temp = temperature

        if temperature < self.min_temp:
            self.min_temp = temperature

        self.display()

    def display(self):
        avg_temp = self.temp_sum / self.num_readings
        print(f"Avg/Max/Min temperature = {avg_temp}/{self.max_temp}/{self.min_temp}")


if __name__ == "__main__":
    weather_station = WeatherStation()

    current_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()

    weather_station.register_observer(current_display)
    weather_station.register_observer(statistics_display)

    weather_station.set_measurements(80, 65, 30.4)
    weather_station.set_measurements(82, 70, 29.2)
    weather_station.set_measurements(78, 90, 29.2)
