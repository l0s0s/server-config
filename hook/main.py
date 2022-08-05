import git
import os
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/hook/push',methods=['POST'])
async def push_hook():
    await update_services()

    return Response(status=200)

async def update_services():
    git.cmd.Git().fetch('https://github.com/l0s0s/server-config','master')
    git.cmd.Git().pull('https://github.com/l0s0s/server-config','master')
    os.system('docker-compose up -d --force-recreate')

if __name__ == '__main__':
    app.run(port=8080)
