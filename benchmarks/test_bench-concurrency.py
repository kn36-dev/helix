import time
from typing import Any

def dummy_processing() -> None:
    """Simulate a minute micro-operation overhead."""
    _ = [x * 2 for x in range(1000)]

def test_benchmark_baseline(benchmark: Any) -> None:
    """Verify that pytest-benchmark is capturing microsecond execution metrics."""
    benchmark(dummy_processing)