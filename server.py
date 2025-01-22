import http.server
import json
import time

import psutil

prev_cpu_info = psutil.cpu_times()


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global prev_cpu_info

        cpu_info = psutil.cpu_times()
        vm_info = psutil.virtual_memory()
        cpu_user = cpu_info.user - prev_cpu_info.user
        cpu_system = cpu_info.system - prev_cpu_info.system
        cpu_idle = cpu_info.idle - prev_cpu_info.idle

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            'cpu_user': cpu_user / (cpu_user + cpu_system + cpu_idle),
            'cpu_all': (cpu_user + cpu_system) / (cpu_user + cpu_system + cpu_idle),
            'memory_used': vm_info.used / vm_info.total,
            'memory_all': 1 - vm_info.free / vm_info.total,
        }).encode())

        prev_cpu_info = cpu_info

    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    httpd = http.server.HTTPServer(('127.0.0.1', 8080), Handler)

    while True:
        try:
            httpd.serve_forever()
        except Exception as e:
            pass

        time.sleep(1)
