from csg2d import Vector

def test_lerp():
    v1 = Vector(0, 10)
    v2 = Vector(0, -10)

    v3 = v1.lerp(v2, .5)

    assert v3.x == 0
    assert v3.y == 0
