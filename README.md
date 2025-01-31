# gRPC-Weather-Service
A Small mock of gRPC service. The weather_server.py produces randomized mock weather data every 2 seconds. A simple client recieves and prints out the data. 

Reasoning why I chose this technology:
gRPC provides clear advantages over REST APIs in the context of sustainability and green programming due to its efficient use of network resources, smaller payload sizes, optimized communication patterns, and reduced CPU and memory usage. By adopting gRPC, organizations can build more resource-efficient systems, which translates to lower energy consumption and a smaller carbon footprint. In contrast, REST APIs may lead to higher operational costs and environmental impact, especially in large-scale or resource-intensive applications. Also I have never tried gRPC but have some familiarity with REST API's, so this was a fun little experiment and learning opportunity.

install required packages:
`pip install -r requirements.txt`

Generate gRPC Python code:
`python -m grpc_tools.protoc -I=proto --python_out=proto --grpc_python_out=proto proto/weather.proto`

Run the weather server in a separate terminal:
`python3 server\weather_server.py`

Run the weather client in a separate terminal:
`python3 server\weather_client.py`

Expected output (values randomized):
+ City: Joensuu, Temperature: -24.290000915527344°C, Humidity: 27%, + Condition: Windy, Timestamp: 2025-01-31T18:36:37.729060
+ City: Turku, Temperature: 15.829999923706055°C, Humidity: 10%, Condition: Rainy, Timestamp: 2025-01-31T18:36:39.738975
+ City: Joensuu, Temperature: 12.479999542236328°C, Humidity: 12%, Condition: Overcast, Timestamp: 2025-01-31T18:36:41.744720
+ City: Joensuu, Temperature: -4.369999885559082°C, Humidity: 57%, Condition: Windy, Timestamp: 2025-01-31T18:36:43.748028