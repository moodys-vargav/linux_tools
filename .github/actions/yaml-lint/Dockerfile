FROM python:3-alpine

LABEL "maintainer"="Viktor Varga <viktor@varga.io>"

LABEL "com.github.actions.name"="yaml-lint"
LABEL "com.github.actions.description"="Run YAML Lint"
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="gray-dark"


RUN pip install 'yamllint>=1.25.0' && \
    apk add --no-cache bash && \
    rm -rf ~/.cache/pip

ADD entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
