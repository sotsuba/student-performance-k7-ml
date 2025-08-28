# Proactively Support Student Success

# __Table of Contents__
**[1. Introduction](#introduction)**

**[2. Repository's structure](#repositorys-structure)**

**[3. Prerequisites](#prerequisites)**

**[4. Local Setup](#local-setup)**

# Introduction

This is the capstone project of K7-Machine Learning - Full Stack Data Science, mentored by Quan Huynh.

# __Repository’s structure__
```
.
├── consumer                # Consumer data from RabbitMQ (predict the data)
│   ├── predict.py
│   └── utils.py
├── core
│   ├── cli.py
│   ├── custom_feature.py
│   └── queue.py
├── data                    # Input data
│   └── student_data.csv
├── docker-compose.yaml     # Run both producer (fake-stream data) + RabbitMQ.
├── Makefile                # Stores useful commands' shortcut.
├── models                  # Store architectures
├── notebooks
│   └── main.ipynb
├── producer                # Producer to RabbitMQ (fake-stream data)
│   ├── data_sample.csv
│   ├── Dockerfile
│   ├── producer.py
│   └── utils.py
└── README.md               # This file
```
# __System Architecture__

<img width="2140" height="725" alt="Screenshot From 2025-08-28 01-37-35" src="https://github.com/user-attachments/assets/11bc2481-fbcf-4b2b-b2a6-c7babebcb586" />

# __Prerequisites__

- Python 3.10
- Docker Engine or Docker Desktop (both is okay, Docker Desktop should be more friendly because of its GUI).
  - Check this out: [How to install Docker Engine](https://docs.docker.com/engine/install/)
# __Local Setup__

**Step 1:** Run producer and RabbitMQ, expose the queue 'alicpp_records' so that producer can send requests into and consumer can get the request to process. 
```bash
# Run producer (push data stream to RabbitMQ) and RabbitMQ, expose the queue 'alicpp_records'
make build_up
```
https://github.com/user-attachments/assets/e9a381a9-a3f4-470f-bb3e-913f6a77969a

**Step 2:** Run consumer to process requests received from RabbitMQ queue 'alicpp_records'
```bash
# Run consumer to receives requests sent by RabbitMQ from producer.
make run_consumer
```
https://github.com/user-attachments/assets/878d3acf-0357-436b-a923-840601c7e253

**Step 3 (Optional):** Check RabbitMQ or Producer logs for debugging.
```bash
  # For RabbitMQ.
  docker logs rabbitmq:3-management
  # For Producer.
  student-performance-producer
```

**Step 4:** Access RabbitMQ Dashboard.
```bash
# RabbitMQ dashboard
http://localhost:15672
```

<img width="2541" height="1367" alt="image" src="https://github.com/user-attachments/assets/985f0af8-0664-432e-a80a-c13f33ee4d97" />



**Step 5:** Shutdown the RabbitMQ and Producer if needed.
```bash
# RabbitMQ dashboard
make down
```
https://github.com/user-attachments/assets/a79fe456-ddf5-4eb7-b7cf-11ce9f0c858e

