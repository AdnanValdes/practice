from sys import argv
import pandas as pd

def main():
    
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    df = pd.read_csv(argv[1])
    STRs = df.loc[:, df.columns != 'name'].columns

    for STR in STRs:
        for i in range(len(df)):

            try:
                if df.iloc[i][STR] != countSTR(STR, argv[2]):
                    # Check that there is only one max value
                    df = df[df.name != df.iloc[i]['name']]
            
            except IndexError:
                break

    if len(df) == 1:
        print(df['name'].values[0])
        exit(0)

    print("No match")

def countSTR(STR, sequence):
    str_count = 0
    str_count_arr = []
    str_len = len(STR)

    with open(sequence, "r") as seq:
        seq = seq.read()
        seq_len = len(seq)
       
        i = 0 
        while i < seq_len:
            current = seq[i:i+str_len]
            if current == STR:
                str_count += 1
                i += str_len

                if i == seq_len:
                    str_count_arr.append(str_count)
            else:
                if str_count > 0:
                    str_count_arr.append(str_count)
                i += 1
                str_count = 0
        if len(str_count_arr) == 0:
            return 0
        return max(str_count_arr)              
   
if __name__ == "__main__":
    main()
