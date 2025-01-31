import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proto')))
import grpc
import time
import random
from concurrent import futures
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from weather_pb2 import WeatherResponse
from weather_pb2_grpc import WeatherServiceServicer, add_WeatherServiceServicer_to_server

class WeatherService(WeatherServiceServicer):
    def StreamWeather(self, request, context):
        cities = ["Tampere", "Helsinki", "Turku", "Oulu", "Joensuu"]
        while True:
            city = random.choice(cities)
            temperature = round(random.uniform(-25, 40), 2)
            humidity = random.randint(10, 100)
            condition = random.choice(["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Overcast","Foggy"])
            # Create a Timestamp object and assign the current UTC time
            timestamp = Timestamp()
            timestamp.FromDatetime(datetime.now())  # Convert datetime to google.protobuf.Timestamp
            
            weather_data = WeatherResponse(
                city=city,
                temperature=temperature,
                humidity=humidity,
                condition=condition,
                timestamp=timestamp
            )
            
            yield weather_data
            time.sleep(2)

# gRPC Server Setup
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Weather gRPC server running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
