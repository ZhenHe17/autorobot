const axios = require('axios')
const req = async (x, y) => {
    const res = await axios.default.get('http://localhost:1134/controlMouseAndKeyboard', {
        params: {
            x,
            y,
            duration: 0.5,
            action: 'move'
        }
    })
    console.log('res', res)
}

const $x = document.querySelector('#x')
const $y = document.querySelector('#y')
const $btn = document.querySelector('#btn')
let ws = null

$btn.addEventListener('click', () => {
    req($x.value, $y.value)
    ws = ws || createWS();
    ws.send("hello")
})

const createWS = () => {
    const _ws = new WebSocket("ws://localhost:1134/ws")
    console.log('ws', _ws)
    //申请一个WebSocket对象，参数是服务端地址，同http协议使用http://开头一样，WebSocket协议的url使用ws://开头，另外安全的WebSocket协议使用wss://开头
    _ws.onopen = function () {
        //当WebSocket创建成功时，触发onopen事件
        console.log("open");
    }
    _ws.onmessage = function (e) {
        //当客户端收到服务端发来的消息时，触发onmessage事件，参数e.data包含server传递过来的数据
        console.log(e.data);
    }
    _ws.onclose = function (e) {
        //当客户端收到服务端发送的关闭连接请求时，触发onclose事件
        console.log("close");
    }
    _ws.onerror = function (e) {
        //如果出现连接、处理、接收、发送数据失败的时候触发onerror事件
        console.log(e);
    }
    return _ws
}

