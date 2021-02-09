# printar alla kombinationer så man har koll
def printsets():
    sets = """
        Calculate a Farkle score using the traditional scoring method, which is:
        4 of any number:              1,000 points
        5 of any number:              2,000 points
        6 of any number:              3,000 points
        1-6 straight:                 1,500 points
        Three pairs:                  1,500 points
        Four of any number + pair:    1,500 points
        Two triplets:                 2,500 points
        Single 1:                     100 points
        Single 5:                     50 points
        Triple of any non-1 number:   100 x number showing
        Triple of ones:               300

        Notes:
        - Doubles score nothing (unless a 1 or a 5) as above
        - All scoring dice must be rolled in a single turn (i.e. they
        are not additive over turns)"""
    print(sets)
