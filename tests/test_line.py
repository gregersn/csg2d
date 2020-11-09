from csg2d.vector import Vector
from csg2d.line import Line
from csg2d.segment import Segment

def test_from_points():
    l = Line.from_points(Vector(0, 0), Vector(0, 10))

    assert l.origin.x == 0
    assert l.origin.y == 0

    assert l.direction.x == 0
    assert l.direction.y == 1

    l = Line.from_points(Vector(0, 0), Vector(5, 0))

    assert l.origin.x == 0
    assert l.origin.y == 0

    assert l.direction.x == 1
    assert l.direction.y == 0

def test_clone():
    l = Line(Vector(0, 0), Vector(1, 0))
    l2 = l.clone()

    assert l is not l2


def test_flip():
    l = Line.from_points(Vector(0, 0), Vector(0, 10))

    assert l.origin.x == 0
    assert l.origin.y == 0

    assert l.direction.x == 0
    assert l.direction.y == 1

    l.flip()

    assert l.origin.x == 0
    assert l.origin.y == 0

    assert l.direction.x == 0
    assert l.direction.y == -1


def test_split_segment():
    s = Segment([Vector(-10, 0), Vector(10, 0)])

    line = Line.from_points(Vector(0, 0), Vector(0, 10))

    coright = []
    coleft = []
    right = []
    left = []
    line.split_segment(s, coright, coleft, right, left)

    assert not coright
    assert not coleft

    assert right
    assert left

    assert len(right) == 1
    assert len(left) == 1

    assert right[0].vertices[0].x == -10.0
    assert right[0].vertices[0].y == 0.0

    assert right[0].vertices[1].x == 0.0
    assert right[0].vertices[1].y == 0.0

    assert left[0].vertices[0].x == 0.0
    assert left[0].vertices[0].y == 0.0

    assert left[0].vertices[1].x == 10.0
    assert left[0].vertices[1].y == 0.0


    s = Segment([Vector(5, 0), Vector(10, 0)])

    line = Line.from_points(Vector(0, 0), Vector(0, 10))

    coright = []
    coleft = []
    right = []
    left = []
    line.split_segment(s, coright, coleft, right, left)


    assert not coright
    assert not coleft

    assert not right
    assert left

    assert len(right) == 0
    assert len(left) == 1


def test_split_segment_2():
    segments = [
        Segment([Vector(0, 0), Vector(0, 10)]),
        Segment([Vector(0, 10), Vector(10, 10)]),
        Segment([Vector(10, 10), Vector(0, 0)])    
    ]

    line = segments[0].line.clone()

    right = []
    left = []
    seg = []
    
    for segment in segments:
        line.split_segment(segment, seg, seg, right, left)
    
    assert len(seg) == 1, seg
    assert len(right) == 0, right
    assert len(left) == 2, left


def test_split_segment_3():
    segments = [
        Segment([Vector(0, 10), Vector(10, 10)]),
        Segment([Vector(10, 10), Vector(0, 0)])    
    ]

    line = segments[0].line.clone()

    right = []
    left = []
    seg = []
    
    for segment in segments:
        line.split_segment(segment, seg, seg, right, left)
    
    assert len(seg) == 1, seg
    assert len(right) == 0, right
    assert len(left) == 1, left


def test_split_segment_4():
    segments = [
        Segment([Vector(10, 10), Vector(0, 0)])
    ]

    line = segments[0].line.clone()

    right = []
    left = []
    seg = []
    
    for segment in segments:
        line.split_segment(segment, seg, seg, right, left)
    
    assert len(seg) == 1, seg
    assert len(right) == 0, right
    assert len(left) == 0, left


def test_split_segments():
    right = []
    left = []
    seg = []
    
    segments = [
        Segment([Vector(0, 0), Vector(0, 10)]),
        Segment([Vector(0, 10), Vector(10, 10)]),
        Segment([Vector(10, 10), Vector(0, 0)]),
    ]

    line = segments[0].line.clone()

    for segment in segments:
        line.split_segment(segment,
                                seg,
                                seg,
                                right,
                                left)
