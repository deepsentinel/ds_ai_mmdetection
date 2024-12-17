FROM nvcr.io/nvidia/pytorch:24.10-py3

# (Optional, use Mirror to speed up downloads)
# RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/mirrors.aliyun.com\/ubuntu\//g' /etc/apt/sources.list && \
#    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Install the required packages
RUN apt-get update \
    && apt-get install -y ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install MMEngine and MMCV
RUN pip install --upgrade pip && pip install opencv-python==4.7.0.72
    
RUN pip install openmim && \
    mim install "mmpretrain"

# Install MMDetection
WORKDIR /mmdetection
COPY . .
RUN pip install --no-cache-dir -e '.[mim]'

WORKDIR /mmdetection
