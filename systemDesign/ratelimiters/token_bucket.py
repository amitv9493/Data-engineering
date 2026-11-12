import time

from pydantic import BaseModel


class ClientData(BaseModel):
    bucket_capacity: int
    timestamp: int
    client_key: str


class KVStore(BaseModel):
    clients: list[ClientData] = []

    def get(self, client: str) -> ClientData | None:
        for cl in self.clients:
            if cl.client_key == client:
                return cl

    def set(self, client_data: ClientData):
        data = self.get(client_data.client_key)
        if not data:
            self.clients.append(client_data)
        else:
            data.bucket_capacity = client_data.bucket_capacity
            data.timestamp = client_data.timestamp


KVSTORE = KVStore()


class TokenBucketRateLimiter:
    def __init__(self, refill_rate: float, capacity: int, consume_tokens_per_req: int):
        self.refill_rate = refill_rate
        self.capacity = capacity
        self.consume_tokens_per_req = consume_tokens_per_req

    def _get_kv_key(self, client) -> str:
        return f"token:rate_limiter:{client}"

    def apply(self, client):
        key = self._get_kv_key(client)

        data = KVSTORE.get(key)

        if not data:
            data = ClientData(
                bucket_capacity=self.capacity,
                timestamp=int(time.time()),
                client_key=key,
            )

        # refill tokens
        time_diff = abs(int(time.time()) - data.timestamp)
        print(f"time diff is {time_diff}")
        tokens = round(time_diff * self.refill_rate)
        print(f"tokens are {tokens}")
        bucket_capacity = min(data.bucket_capacity + tokens, self.capacity)
        allowed = False

        if self.consume_tokens_per_req <= bucket_capacity:
            bucket_capacity = bucket_capacity - self.consume_tokens_per_req
            allowed = True

            KVSTORE.set(
                ClientData(
                    bucket_capacity=bucket_capacity,
                    timestamp=int(time.time()),
                    client_key=key,
                )
            )
        return allowed
