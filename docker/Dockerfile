ARG IMG_NAME=nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04
FROM $IMG_NAME as nvidia-cuda

# Install packages
RUN echo "Installing apt packages..." \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt -y update --no-install-recommends \
    && apt -y install --no-install-recommends \
    apt-utils \
    software-properties-common \
    locales \
    locales-all \
    tzdata \
    sudo \
    curl \
    wget \
    ssh \
    gcc \
    git \
    git-lfs \
    libxrender1 libxext6 \
    # python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    python3-wheel \
    python3-distutils \
    python3-setuptools \
    libcairo2-dev \
    make \
    libssl-dev \
    ncurses-dev \
    libffi-dev \
    libreadline-dev \
    sqlite3 libsqlite3-dev \
    tk-dev \
    bzip2 libbz2-dev \
    lzma liblzma-dev \
    && apt autoremove -y \
    && apt clean \
    && rm -rf /tmp/* \
    /var/tmp/* \
    /var/lib/apt/lists/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base \
    && export DEBIAN_FRONTEND=dialog

# Set location and lang
ARG TZ=Europe/Moscow
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && echo "LC_ALL=en_US.UTF-8" >> /etc/environment \
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "LANG=en_US.UTF-8" > /etc/locale.conf \
    && locale-gen en_US en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 \
    && dpkg-reconfigure -f noninteractive locales 

# Add user
ARG USERNAME
ARG USERPASSWORD
RUN echo "Append $USERNAME to system ..." \
    && groupadd --gid=1000 $USERNAME \
    && useradd -d /home/$USERNAME -s /bin/bash -m $USERNAME -u 1000 -g 1000 \
    && echo $USERNAME:$USERPASSWORD | chpasswd \
    && usermod -aG sudo $USERNAME \
    && echo "$USERNAME  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/$USERNAME
ENV HOME /home/$USERNAME
ENV PATH "$HOME/.local/bin:$PATH"
USER $USERNAME

# Install pyenv
ARG PYVER
RUN curl https://pyenv.run | bash \
    && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
    && echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
    && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
    && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile \
    && echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile \
    && echo 'eval "$(pyenv init -)"' >> ~/.profile \
    && $HOME/.pyenv/bin/pyenv install $PYVER

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true \
    && poetry completions bash >> ~/.bash_completion

CMD ["/bin/bash"]