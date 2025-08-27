# Loss Teach GDGAIC: Blast Fragment Segmentation

# __Table of Contents__
**[1. Introduction](#introduction)**
- _[1.1 About us](#about-us)_
- _[1.2 Overview](#overview)_
- _[1.3 Features](#features)_

# Introduction
Capstone project K7-Machine Learning - Full Stack Data Science.
### Mentor
* Quan Huỳnh 
## Overview

## Features
---
# __Technical Details__
## __Repository’s structure__
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
## __System Architecture__
- In coming
  - `include_mask`: True by default. You can set it to False whenever you need a smaller response for debugging purpose.
  - `include_metrics`: Debugging setting, False by default.
