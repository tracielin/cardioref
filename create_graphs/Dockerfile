# https://hub.docker.com/_/python
FROM python:3.9-alpine

# the only Python dependency is pygraphviz.
# pygraphviz depends on graphviz
# graphviz depends on gcc?

# https://pkgs.alpinelinux.org/package/edge/community/x86/py3-pygraphviz
# https://github.com/pygraphviz/pygraphviz/issues/141
# font issues -- each character is square, as per https://community.atlassian.com/t5/Marketplace-Apps-Integrations/graphviz-text-showing-up-as-squares/qaq-p/85693
RUN apk add --no-cache py3-pygraphviz graphviz graphviz-dev gcc musl-dev make ttf-freefont


# specify which files are required (rather than COPY . /opt)
#COPY browse_internet.py \
#     generate_graphviz.py \
#     requirements.txt \
#     Makefile \
#     /opt/
#WORKDIR /opt

#RUN pip install -r requirements.txt
RUN pip install pygraphviz

WORKDIR /scratch
