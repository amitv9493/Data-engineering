from typing import Any
import redis

def redis_connection():
    yield redis.Redis(host='localhost', port=6379,decode_responses=True)

def smallest_multiple(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

def func(array:list):
    array.sort()
    last_num = array[-1]
    result = []
    for i in range(last_num):
        if i not in array:
            result.append(i)
    
    return result

    
print(func([0,1,3,4,5,7]))

NATIVE_ATTRIBUTES = {'class_name'}
class Root:
    def __init__(self) -> None:
        self.class_name = self,__class__.__name__.lower()
    
    def get_redis_key_path(self, key):
        return "{}.{}".format(self.class_name,key)
    
    def __getattr__(self, key) -> Any:
        if key in NATIVE_ATTRIBUTES:
            return self.__dict__[key]        
        else:
            key = self.get_redis_key_path(key)
            return Lazy(key)
        
    def __setattr__(self, key: str, value: Any) -> None:
        if key in NATIVE_ATTRIBUTES:
            self.__dict__[key] = value
        else:
            key = self.get_redis_key_path(key)
            r.set(key,value)
     


class Lazy:
    def __init__(self,key) -> None:
        self.key= key 
    
    @property
    def value(self):
        return r.get(self.key)
    
    def __repr__(self) -> str:
        return "<Lazy {}>".format(self.key)

    def __str__(self) -> str:
        return self.value

        
# root = Root()
# root.something = 10
# print(root.something)
