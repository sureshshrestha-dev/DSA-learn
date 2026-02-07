from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def get_hits(self, timestamp: int) -> int:
        # Window is [timestamp - 300 + 1, timestamp]
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)

if __name__ == "__main__":
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    assert counter.get_hits(4) == 3
    counter.hit(300)
    assert counter.get_hits(300) == 4
    assert counter.get_hits(301) == 3 # hit at 1 expired
    print("Hit Counter tests passed!")
