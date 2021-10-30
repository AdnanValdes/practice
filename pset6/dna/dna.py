import re

def main():
    countSTR('TA', './sequences/1.txt')

def countSTR(STR, sequence):
    str_count = 0
    str_len = len(STR)

    with open(sequence, "r") as seq:
        seq = seq.read()
        seq_len = len(seq)
        
        str_count = regexRecurse(seq, STR)
        print(str_count)

def regexRecurse(substring, STR):
    count = 0
    match = re.search(STR, substring)

    if not match:
        return count + 1
    
    end_idx = match.span()[1]
    count += 1
    if substring[end_idx:end_idx + len(STR)] == STR:
        count += regexRecurse(substring[end_idx:], STR)
        return count
    else:
        return regexRecurse(substring[end_idx:], STR)


if __name__ == "__main__":
    main()
