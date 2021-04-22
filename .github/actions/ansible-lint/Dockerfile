FROM python:3.8-slim

LABEL "maintainer"="Viktor Varga <viktor@varga.io>"

LABEL "com.github.actions.name"="ansible-lint"
LABEL "com.github.actions.description"="Run Ansible Lint"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="gray-dark"

RUN apt-get update && apt-get -q install -y -V git && rm -rf /var/lib/apt/lists/*
RUN pip install ansible ansible-lint requests

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
