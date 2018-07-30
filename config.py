import redis
import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://name:password@host:port/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis配置
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 8
    # session
    SECRET_KEY = "hellomengf"
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 14  # session 的有效期，单位是秒
    # 项目在磁盘上的目录
    #__file__====>'config.py'
    #os.path.abspath('')==>文件的绝对路径，如/home/python/Desktop/sy8/sy8_flask/xjzx/config.py
    #os.path.dirname('')==>获取目录名，如/home/python/Desktop/sy8/sy8_flask/xjzx
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # 头像保存路径
    AVATAR_PATH = os.path.join(BASE_DIR, 'static/news/images/')

    # 腾讯云cos
    QCLOUD_secret_id = 'AKIDdAaqxtPunX7azCQ3OoLl1Mkz42umiEln'      # 替换为用户的 secretId
    QCLOUD_secret_key = 'PwSoIigVRYm6FJDynbOQi7ThU7Zry87F'      # 替换为用户的 secretKey
    QCLOUD_region = 'ap-beijing'   # 替换为用户的 Region
    QCLOUD_token = 'flask_news'
    QCLOUD_Bucket = 'flask-news-1251357287'
    QCLOUD_SRC_URL = 'http://flask-news-1251357287.cosbj.myqcloud.com/'

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://test:mysql@localhost:3306/flask_news'


class ProductConfig(Config):
    pass