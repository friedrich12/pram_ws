# To build use:
# docker build -t dems .

# docker network create --driver bridge --ipv6 --subnet 2a02:6b8:b010:9020:1::/80 ipv6_dems
# docker create --name dems0 --network ipv6_dems --ip ipv4address  -t -i dems
# and create other containers

#$ docker start -a -i 6d8af538ec5

# docker inspect <container name or container id>



FROM ubuntu:18.04
#ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y git python3-pip python3-psutil
RUN pip3 install pip install git+https://github.com/momacs/pram.git
RUN pip3 install attrs --upgrade
RUN git clone https://github.com/momacs/pram
RUN cd pram/src/sim/01-simple && python3 sim.py


