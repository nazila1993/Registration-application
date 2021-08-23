def f(*args):
    return max(args) - min(args), sum(args)
def test(cases):
    for i in cases :
        assert f(*cases[0]) == cases[1], cases[2]





cases =  [
    [(1,2,3,4,5,6,7,8,9,10),(9, 55), "9, 55"],
    [(2,10,1,11,11,32,42,21,32,23), (41, 185), "41, 185"],
    [(3,'g','e','s',7,12,'e','s','x','!'), None, 'Error']
]

