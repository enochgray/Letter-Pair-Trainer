import csv, random

def reset():

    a = []

    for i in range(23):
        a.append([])
        for j in range(24):
            a[i].append(0)

    list_to_csv("paircount.csv",a)

def test():

    total_min = 5
    streak_min = 3
    num_pairs = 3

    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

    arr_total = []
    arr_streak = []
    arr_words = []
    csv_to_list("lptotal.csv",arr_total)
    csv_to_list("lpstreak.csv",arr_streak)
    csv_to_list("lpwords.csv",arr_words)
    
    idx1 = 0
    idx2 = 0
    arr_1 = []
    arr_2 = []
    lp = ""
    ws = ""

    for i in range(num_pairs):

        bool_max = True

        while bool_max:
            idx1 = random.randint(0,22)
            idx2 = random.randint(0,23)
            if int(arr_total[idx1][idx2]) < total_min or int(arr_streak[idx1][idx2]) < streak_min:
                bool_max = False
                
        arr_1.append(idx1)
        arr_2.append(idx2)
        lp = lp + abc[idx1] + abc[idx2] + " "
        ws = ws + arr_words[idx1][idx2] + " "
        
    print(lp)
    incorrect = input()
    print(ws)
    
    incorrect = input()
    i = 1
    if incorrect != 'q':
        for i in range(num_pairs):
            if incorrect.find(str(i+1))!=-1:
                arr_streak[arr_1[i-1]][arr_2[i-1]] = 0
            else:
                arr_streak[arr_1[i-1]][arr_2[i-1]] = int(arr_streak[arr_1[i-1]][arr_2[i-1]]) + 1
                arr_total[arr_1[i-1]][arr_2[i-1]] = int(arr_total[arr_1[i-1]][arr_2[i-1]]) + 1
            i = i + 1
    
    list_to_csv("lptotal.csv",arr_total)
    list_to_csv("lpstreak.csv",arr_streak)

def main(n):

    max_num = 2
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

    a = []
    csv_to_list("paircount.csv",a)
    idx1 = 0
    idx2 = 0
    lp = ""

    for i in range(n):

        bool_max = True

        while bool_max:
            idx1 = random.randint(0,22)
            idx2 = random.randint(0,23)
            if int(a[idx1][idx2]) < max_num:
                bool_max = False
                a[idx1][idx2] = int(a[idx1][idx2]) + 1
                
        lp = lp + abc[idx1] + abc[idx2] + " "
        
    print(lp)

    list_to_csv("paircount.csv",a)
    
def list_to_csv(write_name,write_list):

    with open(write_name,'w',newline="") as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for row in write_list:
            writer.writerow(row)

def csv_to_list(write_name,write_list):

    with open(write_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            write_list.append(row)
