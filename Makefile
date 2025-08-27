.PHONY: run_consumer, run_producer, remove_queue, composed

run_consumer:
	python -m consumer.predict --rabbitmq_server localhost --queue_name alicpp_records

run_producer:
	python -m producer.producer --mode setup --rabbitmq_server localhost

remove_queue:
	python -m producer.producer --mode teardown --rabbitmq_server localhost

composed:
	