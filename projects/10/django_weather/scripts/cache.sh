sudo apt-get update
sudo apt install -y redis
sudo systemctl status redis
redis-cli --version
redis-cli
# PING (PONG)
exit


pip install django_redis
pip freeze > requirements.txt
# "extra": {
#     "BACKEND": "django_redis.cache.RedisCache",
#     "LOCATION": "redis://127.0.0.1:6379/1",
#     'TIMEOUT': '600',
#     "OPTIONS": {
#         "CLIENT_CLASS": "django_redis.client.DefaultClient",
#     }
# }  

# DatabaseCache = caches["default"]
# LocMemCache = caches["special"]
# RedisCache = caches["extra"]

# caches_res = ""
# caches_res = "Cache find"
# users = RedisCache.get("hotNews")
# if users is None:
#     caches_res = "Cache not found"
#     users = User.objects.all()
#     RedisCache.set("hotNews", users, timeout=5)
