#!/bin/bash
# This shell script deploys a new version to our server.

echo "SSHing to PythonAnywhere."
sshpass -p $SERV_PW ssh -o "StrictHostKeyChecking no" nathanconroydev@ssh.pythonanywhere.com << EOF
    cd /home/nathanconroydev/MyWebsiteBackend; API_TOKEN=$SERV_API_TOKEN ./rebuild.sh
EOF
