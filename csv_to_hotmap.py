import csv
import pandas as pd
import sys
import numpy as np
import getopt
import seaborn

'-f file '

def do():
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "f:h")

    except:
        print("Error")


    filename = ''


    for opt, arg in opts:
        if opt in ['-f']:
            filename = arg
        elif opt in ['-h']:
            print('''-f filename ''')
    col_list = list(range(1,21))
    df = pd.read_csv(filename,usecols=col_list)

    resnumbers = []
    path = '../'
    pylist = os.listdir(path)
    for file in pylist:
        if '.py' in file:
            file_name = file.strip('.py')
            if file_name.isdigit() == 1:
                resnumbers.append(file_name)
    
    residue_codes = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    ar = np.array(df)
    new_df = pd.DataFrame(ar,index=resnumbers,columns=residue_codes)
    print(df)
    print(ar)
    print(new_df)
    hm = seaborn.heatmap(new_df,vmin=-3,vmax=3,center=0,cmap=None)
    s1 = hm.get_figure()
    s1.savefig('1.jpg')

do()
