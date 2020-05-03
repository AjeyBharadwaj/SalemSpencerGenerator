import pdb
import sys

def fill_next(Series, Diff, Max):
    Cur = Series[-1]

    for i in range(Cur+1, Max+1):
        CanAdd = True

        # See if D is already there.
        for j in Diff:
            D = i - j
            if D in Diff[j]:
                CanAdd = False
                break

        if CanAdd is True:
            # Now I can add
            for j in Diff:
                D = i - j
                Diff[j].append(D)

            Series.append(i)

            Diff[i] = []
            for j in Series:
                Diff[i].append(i - j)

            return True, Series, Diff

    return False, Series, Diff


def init(Start, End):
    Series = []
    Series.append(int(Start))

    Diff = {}
    Diff[int(Start)] = [0]

    return Series,Diff

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python3 main.py Start End")
    else:
        Series,Diff = init(sys.argv[1], sys.argv[2])

        while True:
            to_continue, Series, Diff = fill_next(Series, Diff, int(sys.argv[2]))
            if to_continue is False:
                print(Series)
                break
