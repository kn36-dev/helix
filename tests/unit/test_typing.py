import numpy as np
from collections.abc import Buffer
from helix.core.typing import TensorLike

class CustomMockTensor:
    """A manual mock class that implements the TensorLike structure."""
    def __init__(self, dimensions: tuple[int, ...]):
        self._matrix = np.zeros(dimensions, dtype=np.float32)
        
    @property
    def shape(self) -> tuple[int, ...]:
        return self._matrix.shape

    @property
    def nbytes(self) -> int:
        return self._matrix.nbytes

    def as_buffer(self) -> Buffer:
        # memoryview exposes raw memory without copying data bytes
        return memoryview(self._matrix)

def test_structural_conformance_checks() -> None:
    """Verify that objects matching the protocol shape are identified correctly."""
    mock_tensor = CustomMockTensor((2, 512, 512, 3)) # Batch, H, W, C
    
    # Because of @runtime_checkable, isinstance() queries work perfectly!
    assert isinstance(mock_tensor, TensorLike)

def test_numpy_compatibility_loop() -> None:
    """Ensure that standard AI matrices naturally satisfy our custom performance rules."""
    raw_numpy_array = np.random.randn(1, 1536) # LLM Embedding vector layout
    
    # Ducks check out: numpy arrays naturally have shape and implement buffers!
    assert hasattr(raw_numpy_array, "shape")
    assert isinstance(memoryview(raw_numpy_array), Buffer)