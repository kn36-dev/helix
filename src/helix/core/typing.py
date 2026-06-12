from typing import Protocol, runtime_checkable
from collections.abc import Buffer

@runtime_checkable
class TensorLike(Protocol):
    """
    A runtime-checked Protocol that enforces the structural requirements 
    of a performant, zero-copy tensor layout.
    """

    @property
    def shape(self) -> tuple[int, ...]:
        """Returns the dimensions of the tensor (e.g., Batch, H, W, C)."""
        ...

    @property
    def nbytes(self) -> int:
        """Returns the total number of bytes consumed by the elements of the tensor."""
        ...

    def as_buffer(self) -> Buffer:
        """Exposes the underlying raw memory buffer without duplicating bytes."""
        ...