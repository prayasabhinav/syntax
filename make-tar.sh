#!/usr/bin/env bash
# Builds syntax.tar for CapRover: build the site, then pack the Dockerfile and site/.
# Deploy: caprover deploy -n myplaceholder -a syntax -t syntax.tar
set -euo pipefail
cd "$(dirname "$0")"
python3 build.py
COPYFILE_DISABLE=1 tar --exclude='._*' --exclude='.DS_Store' -cf syntax.tar captain-definition Dockerfile nginx.conf site
echo "syntax.tar: $(du -h syntax.tar | cut -f1)"
