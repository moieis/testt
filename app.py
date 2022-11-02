from pywebio.input import *
from pywebio.output import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
def main():
        
        ww = ChromeDriverManager().install()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-gpu')
        a = webdriver.Chrome(executable_path=ww, chrome_options=options)
        
        put_text('hi')

if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(main, port=args.port, websocket_ping_interval=30)

