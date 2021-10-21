from aiohttp import web
import controller

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/controlMouseAndKeyboard', controller.controlMouseAndKeyboard),
                web.get('/t', controller.test),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, port=1134)