FROM python:3.9-slim

# Copy app handler code
COPY producer/producer.py producer.py
COPY producer/utils.py utils.py
COPY producer/data_sample.csv data_sample.py
COPY core/ core/

# Install dependencies
RUN pip3 install pandas==2.2.3
RUN pip3 install pika==1.3.2

# This Dockerfile command runs a Python script named 'producer.py'
# -u: Runs the Python interpreter in unbuffered mode. The script is executed with the 'setup' mode and connects
# to a RabbitMQ server named 'rabbitmq'.
CMD [ "python", "-u", "producer.py", "--mode", "setup", "--rabbitmq_server", "rabbitmq"]