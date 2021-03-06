# coding=utf-8
# 不能在该文件引用django相关类库，执行这里的时候django还未初始化。
# 详细配置说明请参考httpappengine/engine/config.py
DEBUG = False

# 服务器监听地址。
HOST = "0.0.0.0"
PORT = 8888

# 需要载入的Action 模块
ACTIONS = [
    "action",
    #"plugs.qiniudn"
]

SUPPORT_DJANGO = True
DJANGO_SETTINGS_MODULE = "django_demo.settings"
DJANGO_URLS = [
    # "/demo"
]

USE_PDB = True

# ENGINE = "werkzeug"

WORKERS = 1
SUPPORT_WEBSOCKET = False