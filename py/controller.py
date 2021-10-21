from aiohttp import web
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
