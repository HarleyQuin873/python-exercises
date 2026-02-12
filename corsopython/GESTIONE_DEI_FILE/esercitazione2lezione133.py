
with (
    open("isolamisteriosa.txt", "rt") as fin,
    open("outputfile.txt", "a") as fout
    ):
    lines = fin.readlines()
    c = 1
    for l in lines:
        if(c % 2 == 0):
            str = f"{c}:{l}"
            fout.write(str)
        c += 1

