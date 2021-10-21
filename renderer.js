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

$btn.addEventListener('click', () => {
    req($x.value, $y.value)
})
