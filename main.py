import time
from systemDesign.ratelimiters.token_bucket import TokenBucketRateLimiter, KVSTORE


def throttle(repeat: int):
    for i in range(repeat):
        print(rate_limter.apply("client1"))
        print(KVSTORE.clients)
        time.sleep(1)
        print("=" * 50)


if __name__ == "__main__":
    rate_limter = TokenBucketRateLimiter(
        refill_rate=0.5, capacity=5, consume_tokens_per_req=1
    )

    throttle(10)
    time.sleep(10)
    throttle(1)
