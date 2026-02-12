try:
    file_object = open('isolamisteriosa.txt', 'rt')
    lines = file_object.readlines()
    fw = open("outputfile.txt", "w")

    counter = 1
    for line in lines:
        if(counter % 2 == 1):
            str = f"{counter}:{line}"
            fw.write(str)
        counter += 1

finally:
        # Assicurati che il file venga chiuso
         # file_object.close()
    file_object.close()
    fw.close()
