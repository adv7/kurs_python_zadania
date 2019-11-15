# Zadanie dla wszystkich
# =============

# Sprawdzić czy numer VIN jest poprawny w oparciu o checksumę (9 cyfra w ciagu cyfr).

# ======================
# input : plik z numerami VIN
# output : plit z numerem VIN + text+ "VALID" lub "INVALID"

# ASDASDASDG123321 INVALID
# DDSDSDAGVCVCVQQQ INVALID

# Więcj info o numerze VIN
# --------------------------------
# https://en.wikipedia.org/wiki/Vehicle_identification_number


def open_file_download_vins():
    try:
        with open("vins.txt", "r") as opened_file:
            vins = []
            for line in opened_file.readlines():
                if line in ['\n', '\r\n']:
                    continue
                line = line.rstrip().upper()
                vins.append(line)
            return vins
    except IOError:
        print("Error: can\'t find file or read data")


def vin_checker(vins_list):
    for vin in vins_list:
        if ((len(vin) != 17) | (vin.find("O") >= 0) | (vin.find("Q") >= 0) | (vin.find("I") >= 0) | (vin[13:16].isdigit() == False) | ((vin[8].isdecimal() == False) & (vin[8] != "X"))):
            vin_status = False
            vin_to_vin_with_status_replacer_in_vins_list(vin, vins_list, vin_status)
        elif (counting_checksum(vin)):
            vin_status = True
            vin_to_vin_with_status_replacer_in_vins_list(vin, vins_list, vin_status)
        else:
            vin_status = False
            vin_to_vin_with_status_replacer_in_vins_list(vin, vins_list, vin_status)
    return vins_list


def counting_checksum(vin):
    vin_digit_weights = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                         'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
                         'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9,
                         '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

    position_weights = (8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2)

    sum = 0
    loop_index_to_iterate_vin = 0
    for position_weight in position_weights:
        sum += position_weight * vin_digit_weights[vin[loop_index_to_iterate_vin]]
        loop_index_to_iterate_vin += 1

    correct_checksum = sum % 11
    if (correct_checksum == 10):
        correct_checksum = "X"
    if (str(correct_checksum) == vin[8]):
        return True
    else:
        return False


def vin_to_vin_with_status_replacer_in_vins_list(vin, vins_list, status):
    vin_with_status = vin_status_appender(vin, status)
    vins_list[vins_list.index(vin)] = vin.replace(vin, vin_with_status)


def vin_status_appender(vin, status):
    if (status == True):
        line = f"{vin} VALID"
        return line
    else:
        line = f"{vin} INVALID"
        return line


def return_file_conteins_vins_and_them_status(vins_list):
    for vin in vins_list:
        vin_with_endl = f"{vin}\n"
        vins_list[vins_list.index(vin)] = vin.replace(vin, vin_with_endl)
    try:
        with open("vins_checked.txt", "w") as opened_file_to_write:
            opened_file_to_write.writelines(vins_list)
    except IOError:
        print("Error: Oupsiee, something goes totally wrong!")


vins_list = open_file_download_vins()
checked_vins_list = vin_checker(vins_list)
return_file_conteins_vins_and_them_status(checked_vins_list)
print("DONE")
