dupes_err_msg = "Error: multiple keys for same value!"


def dict_has_dupes(dicc: dict):
    if len(dicc) == 0:
        return ("Empty dictionary!")

    return len(set(dicc.values())) != len(dicc)
