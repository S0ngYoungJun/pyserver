from http.server import HTTPServer, SimpleHTTPRequestHandler

# 서버 주소와 포트 설정
host = 'localhost'
port = 8000

# HTTPServer 인스턴스 생성 및 실행
httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Server started at http://{host}:{port}")
httpd.serve_forever()