import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() + 1
print(workers)
timeout = 30
worker_connections = 1000
