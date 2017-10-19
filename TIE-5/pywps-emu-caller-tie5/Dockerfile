FROM docker-registry.crim.ca/ogc/emu:tie5

ENV AMQP_USER guest
ENV AMQP_PASSWORD guest
ENV AMQP_HOST rabbitmq
ENV AMQP_PORT 5672

RUN git clone -b ogc-TIE5 https://github.com/crim-ca/pywps.git
COPY modifconda.sh .
RUN bash modifconda.sh


