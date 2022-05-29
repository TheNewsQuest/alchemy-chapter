FROM python:3.8

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /usr/app/src

COPY requirements.txt build-constraints.txt ./
RUN PIP_CONSTRAINT=build-constraints.txt pip --no-cache-dir install -r requirements.txt
RUN python -m nltk.downloader punkt
ADD . .

CMD ["flask", "run", "--host=0.0.0.0"]