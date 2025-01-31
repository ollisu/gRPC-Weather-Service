import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))
import grpc
from weather_pb2 import WeatherRequest
from weather_pb2_grpc import WeatherServiceStub

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = WeatherServiceStub(channel)
    request = WeatherRequest()

    for weather_update in stub.StreamWeather(request):
        timestamp = weather_update.timestamp.ToDatetime().isoformat()

        print(f"City: {weather_update.city}, Temperature: {weather_update.temperature}°C, "
              f"Humidity: {weather_update.humidity}%, Condition: {weather_update.condition}, "
              f"Timestamp: {timestamp}")

if __name__ == "__main__":
    run()