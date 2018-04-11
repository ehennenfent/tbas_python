def load_string(in_str):
    program = '>'.join('+'*(ord(k)) for k in in_str)
    program += '<'*len(in_str)
    return program