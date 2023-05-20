import http.server
import json
import socketserver
import urllib,urllib.request
API_KEY = "<API_KEY>"
CX = "<CX>"

class SearchDataHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            html = '''<!DOCTYPE html>
                        <html lang="en">
                        <head>
                        <meta charset="UTF-8">
                        <title>1</title>
                        </head>
                        <body>
                        <form method="POST">
                        <label>Поиск:</label><br>
                        <input type="text" name="query" value=""><br>
                        <input type="submit" value="Submit">
                        </form> 
                        </body>
                        </html>
                   '''
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(self.rfile.read(content_length).decode('utf-8'))
        query = post_data.get('query')[0]
        html = '''
                      <!DOCTYPE html>
                        <html lang="en">
                        <head>
                        <meta charset="UTF-8">
                        <title>2</title>
                        </head>
                      <body>
                      <form method="POST">
                      <label>Поиск:</label><br>
                      <input type="text" name="query" value="{}"><br>
                      <input type="submit" value="Submit">
                      </form>
                      {}
                      </body>
                      </html>
                  '''
        url = 'https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}'.format(API_KEY, CX, query)

        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        response.close()
        results = json.loads(data)['items']
        res = ''
        if results:
            res += '<tr>'
            for i in results:
                res += f'<td><a href="{i["link"]}">{i["title"]}</a></td><p>{i["snippet"]}</p>'
            res += '</tr>'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(html.format(query, res), 'utf-8'))
PORT = 8000
httpd = socketserver.TCPServer(("", PORT), SearchDataHandler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()