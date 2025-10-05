def total_size(node):
    """
    Recursively compute the total size of a directory tree.
    Each node is a dict with:
      - type: "file" or "dir"
      - name: string
      - size: (only for file, optional, defaults to 0)
      - children: list of nodes (only for dir)
    """
    # Base case: if node is None
    if node is None:
        return 0

    # Handle file node
    if node.get("type") == "file":
        return node.get("size", 0)

    # Handle directory node
    if node.get("type") == "dir":
        total = 0
        for child in node.get("children", []):
            total += total_size(child)
        return total

    # Unknown type: ignore
    return 0
