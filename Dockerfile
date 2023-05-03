FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt -y upgrade && apt install -y python3 ipython3 python3-pip
RUN pip install --upgrade pip setuptools wheel matplotlib && \
    mkdir IntrosecFuzzing

ENV PYTHONPATH "${PYTHONPATH}:/IntrosecFuzzing"
WORKDIR IntrosecFuzzing
CMD ["/bin/bash"]
