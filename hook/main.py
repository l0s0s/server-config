from time import sleep
import git
import os
import asyncio
from flask import Flask, Response

app = Flask(__name__)

@app.route('/hook/push',methods=['POST'])
async def push_hook():
    await update_services()

    print(1)

    return Response(status=200)

async def update_services():
    await asyncio.sleep(1)

    print(2)

    git.cmd.Git().fetch('https://github.com/l0s0s/server-config','master')
    git.cmd.Git().pull('https://github.com/l0s0s/server-config','master')
    os.system('docker-compose up -d --force-recreate')

if __name__ == '__main__':
    app.run(port=8080)
