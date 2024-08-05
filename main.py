from typing import Any, List, Tuple

class SlowAPI:
    def __init__(self) -> None:
        pass

    def __call__(self, env, start_res) -> List[bytes]:
        print(env)
        headers = [('Content-Type', 'text/plain')]
        start_res("200 OK", headers)
        return [b"Hello, Musharaf"]

    def get(self , path=None):
        def wrapper(handler):
            print(handler,path)   
        return wrapper