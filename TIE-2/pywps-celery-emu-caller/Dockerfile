FROM birdhouse/emu

ENV AMQP_USER guest
ENV AMQP_PASSWORD guest
ENV AMQP_HOST rabbitmq
ENV AMQP_PORT 5672

RUN git clone -b celerydev https://github.com/fderue/pywps.git
COPY modifconda.sh .
RUN bash modifconda.sh


