from aiohttp import web
import aiohttp
import pyautogui

async def test(request):
    pyautogui.moveTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)


async def controlMouseAndKeyboard(request):
    print(request.query)
    x = request.query.get('x')
    y = request.query.get('y')
    action = request.query.get('action')
    key = request.query.get('key')
    duration = request.query.get('duration')
    text = ''
    if(action == 'move'): 
        pyautogui.moveTo(int(x), int(y), duration=float(duration), tween=pyautogui.easeInOutQuad)
        text = action + " (" + x + "," + y + ")"
    if(action == 'press'):
        pyautogui.press(key)
        text = action + " (" + key + ")"

    return web.Response(text=text)

async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws