FROM docker-registry.crim.ca/ogc/pywps-emu-caller:tie5

RUN sudo curl -sSL https://get.docker.com/ | sh
COPY run_conda_celery.sh . 

ENV AMQP_USER guest
ENV AMQP_PASSWORD guest
ENV AMQP_HOST rabbitmq
ENV AMQP_PORT 5672
CMD ["bash", "run_conda_celery.sh"]
