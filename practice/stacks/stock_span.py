class StockSpanner:
    def __init__(self):
        # Stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

if __name__ == "__main__":
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    expected = [1, 1, 1, 2, 1, 4, 6]
    results = [spanner.next(p) for p in prices]
    
    print(f"Prices: {prices}")
    print(f"Spans:  {results}")
    assert results == expected
    print("Stock Span tests passed!")
