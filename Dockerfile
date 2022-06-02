FROM python:3.8

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app/src

# Install app's dependencies
COPY requirements.txt build-constraints.txt ./
RUN PIP_CONSTRAINT=build-constraints.txt pip --no-cache-dir install -r requirements.txt
RUN python -m nltk.downloader punkt
COPY . .

# Run Gunicorn HTTP Server
CMD ["sh", "-c", "gunicorn --chdir /usr/app/src api_gateway:app --worker-class=${GUNICORN_WORKER_CLASS} --worker-connections=${GUNICORN_WORKER_CONNECTIONS=} -w ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --limit-request-line 0 -b=0.0.0.0:${APP_PORT} --timeout ${GUNICORN_TIMEOUT}"]