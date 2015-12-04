from languages import language

def input_float(text="", lang="en"):
    lan = language[lang]
    is_num = False
    while is_num == False:
        try:
            num = float(input(text))
            is_num = True
        except ValueError:
            print(lan["error_input_num"])
            is_num = False
        else:
            pass
        finally:
            pass
    return num

def input_int(text="", lang="en"):
    lan = language[lang]
    is_num = False
    while is_num == False:
        try:
            num = int(input(text))
            is_num = True
        except ValueError:
            print(lan["error_input_int"])
            is_num = False
        else:
            pass
        finally:
            pass
    return num