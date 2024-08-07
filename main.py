from typing import Any, List, Tuple

class SlowAPI:
    def __init__(self) -> None:
        self.routes = dict()
         

    def __call__(self, env, start_res) -> List[bytes]:
        print(env)
        headers = [('Content-Type', 'text/plain')]
        start_res("200 OK", headers)
        return [b"Hello, "]

    def get(self , path=None):
        def wrapper(handler):
            path_name = path or f"/{handler.__name__}"  
            if path_name not in self.routes:
                self.routes[path_name] ={}
            self.routes[path_name]['GET'] = handler

            print(self.routes)
        return wrapper
