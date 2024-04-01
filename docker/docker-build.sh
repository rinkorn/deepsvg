#!/bin/bash

IMG_TAG_IN="nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04"
IMG_TAG_OUT="trypyg/cuda:12.2.2-cudnn8-runtime-ubuntu22.04"
TZ="Europe/Moscow"
USERNAME="mluser"
USERPASSWORD="mlpassword"
PYVER="3.10.13"

docker build \
  --no-cache \
  --build-arg IMG_NAME=$IMG_TAG_IN \
  --build-arg TZ=$TZ \
  --build-arg USERNAME=$USERNAME \
  --build-arg USERPASSWORD=$USERPASSWORD \
  --build-arg PYVER=$PYVER \
  --tag $IMG_TAG_OUT \
  .
