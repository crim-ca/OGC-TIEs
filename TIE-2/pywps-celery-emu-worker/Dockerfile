FROM emu_celery_caller

ENV AMQP_USER guest
ENV AMQP_PASSWORD guest
ENV AMQP_HOST rabbitmq
ENV AMQP_PORT 5672

COPY run_conda_celery.sh . 
CMD ["bash", "run_conda_celery.sh"]