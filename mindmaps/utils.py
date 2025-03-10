from .models import Node

def get_mindmap_structure(mindmap):
    """
    Returns a structured dictionary of nodes for visualization.
    """
    nodes = mindmap.nodes.all()
    node_dict = {node.id: {"content": node.content, "children": []} for node in nodes}

    for node in nodes:
        if node.parent:
            node_dict[node.parent.id]["children"].append(node_dict[node.id])

    return node_dict


def create_node(mindmap, content, parent=None, position_x=0, position_y=0):
    """
    Creates a new node under a mind map.
    """
    node = Node.objects.create(
        mindmap=mindmap,
        content=content,
        parent=parent,
        position_x=position_x,
        position_y=position_y
    )
    return node
