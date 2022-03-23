# AutoRobot

Electron 调用 Python 打造桌面应用的 Demo，主要通过 HTTP、WebSocket 建立两者的连接

Demo 功能为调用 输入 x、y 坐标，程序会移动鼠标到屏幕的 x,y 位置。注意：需要授予应用控制权限，在 MacOS 下设置 偏好设置 -> 隐私 -> 辅助功能。

技术栈：NodeJS、Electron、Python、aiohttp（HTTP、WebSocket）、pyautogui（控制鼠标）

## 项目启动

启动命令：

```bash
# 安装 pyinstaller
# pyInstaller: 版本 4.5.1
# python: 版本 3.9.7
pip install pyinstaller
# 把 python 代码打包为可执行文件
npm run build-python
# 安装依赖
npm install
# 启动开发环境
npm start
```
