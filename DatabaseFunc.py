def protein_database_parser(counter):
    database = list()
    file = open("Database.txt", "r")
    temp = ""
    read_flag = False
    for line in file:
        if counter == 0:
            break
        if not line:
            continue
        if line[0] == '>' and not read_flag:
            read_flag = True
            continue
        if line[0] != '>' and read_flag:
            temp += line[:-2]
            continue
        if line[0] == '>' and read_flag:
            database.append(temp)
            temp = ""
            counter -= 1
    file.close()
    return database

