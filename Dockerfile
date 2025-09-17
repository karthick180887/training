FROM bitnami/kafka:3.5.1

USER root

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Switch back to non-root Bitnami user
USER 1001