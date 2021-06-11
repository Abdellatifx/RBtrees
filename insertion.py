import rbtree as rb


def insert(t, z):
    z = rb.Node, x = rb.Node, y = rb.Node
    t = rb.Rbtree
    y = t.nil
    x = t.root
    while x != t.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == t.nil:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = t.nil
    z.right = t.nil
    z.colour = "red"
    insertfixup(t, z)


def insertfixup(t, z):
    z = rb.Node, x = rb.Node, uncle = rb.Node
    t = rb.Rbtree
    while z.parent.colour == "red":
        if z.parent == z.parent.parent.left:
            uncle = z.parent.parent.right
            if uncle.colour == "red":  # recolour
                z.parent.colour = "black"
                uncle.colour = "black"
                z.parent.parent.colour = "red"
                z = z.parent.parent
            elif z == z.parent.right:
                z = z.parent

    t.root.colour = "black"
