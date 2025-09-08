bind = "0.0.0.0:8000"
workers = 4
worker_class = "gthread"
threads = 4
timeout = 120
max_requests = 1000
max_requests_jitter = 100
preload_app = True
