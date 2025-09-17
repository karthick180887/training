FROM bitnami/kafka:3.5.1

# Switch to root
USER root

# Set root password (example: root123)
RUN echo "root:root123" | chpasswd

# Install Python, pip, editors
RUN apt-get update && apt-get install -y python3 python3-pip vim nano && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install kafka-python

# Switch back to non-root user
USER 1001