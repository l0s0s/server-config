import git
import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/hook/push',methods=['POST'])
def push_hook():
    git.cmd.Git().fetch('https://github.com/l0s0s/server-config','master')
    git.cmd.Git().pull('https://github.com/l0s0s/server-config','master')
    os.system('docker-compose up -d --force-recreate')

    return Response(status=200)

if __name__ == '__main__':
    app.run()
