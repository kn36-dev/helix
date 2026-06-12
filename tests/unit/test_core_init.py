import helix

# Check if the helix module has a __version__ attribute; if not, use "0.1.0"
version = getattr(helix, "__version__", "0.1.0")

def test_package_availability() -> None:
    """Ensure the package namespace is resolvable under test environments."""