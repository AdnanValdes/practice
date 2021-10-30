import re

def main():
    countSTR('AA', './sequences/1.txt')

def countSTR(STR, sequence):
    str_count = 0
    str_count_arr = []
    str_len = len(STR)

    with open(sequence, "r") as seq:
        seq = seq.read()
        seq = 'AABBAAAABBCCAAAAAAAAAAAABBDDFAAGGAAAAAAAA'
        seq_len = len(seq)
       
        i = 0 
        while i < seq_len:
            current = seq[i:i+str_len]
            print(current)
            if current == STR:
                print("MATCH!")
                str_count += 1
                i += str_len

                if i == seq_len:
                    str_count_arr.append(str_count)
            else:
                if str_count > 0:
                    str_count_arr.append(str_count)
                i += 1
                str_count = 0
        return max(str_count_arr)               
   
if __name__ == "__main__":
    main()
