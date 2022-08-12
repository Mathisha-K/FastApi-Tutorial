from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/opt/projects/FastApi-Tutorial/src/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/var/log/fastapi-tutorial/access_log'
errorlog =  '/var/log/fastapi-tutorial/error_log'