from sanic import Sanic
from sanic.response import json
from config import Server

app = Sanic(__name__)

srv = Server()

@app.route('/')
async def test(request):
    # print(request)
    # for k, v in request.items():
    #     print('{}  --->  {}'.format(k, v))
    return json('Haha')


if __name__ == "__main__":
    app.run(host=srv.host, port=srv.port, debug=True)