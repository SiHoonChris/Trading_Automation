from statistics import mean, pstdev
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

def trim(df):
    df.sort_index(ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.drop(columns=df.columns[5:], inplace=True)
    return df.index[-1]
    # Turn the descending datas into ascending order
    # Remain the Columns of Date, Price, Open, High, Low, and Remove the last(Vol., Change %)

def SMA_ATR(period, last_idx): # period=250 (1-year)
    TR=[]
    for i in range(0, last_idx+1):
        if i==0:
            TR.append(abs(df.loc[i,'High']-df.loc[i,'Low']))
        else:
            TR1=abs(df.loc[i,'High']-df.loc[i,'Low'])
            TR2=abs(df.loc[i,'High']-df.loc[i-1,'Price'])
            TR3=abs(df.loc[i,'Low']-df.loc[i-1,'Price'])
            TR.append(max(TR1, TR2, TR3))
    ATR=[]
    for i in range(0, last_idx+1):
        if i < (period-1):
            ATR.append("")
        else:
            ATR.append(mean(TR[i-(period-1):(i+1)]))
    for i in range(0, last_idx+1):
        if i < (period-1):
            pass
        else:
            df.loc[i,'SMA-ML']=df.loc[i-(period-1):i, 'Price'].mean()
            df.loc[i,'SMA-UL']=df.loc[i-(period-1):i, 'Price'].mean()+ATR[i]*2
            df.loc[i,'SMA-LL']=df.loc[i-(period-1):i, 'Price'].mean()-ATR[i]*2

class Ichimoku(): # CL=9, BL=26, LS_B=52
    def __init__(self, CL, BL, LS_B, last_idx): # last_idx = df.index[-1] #which is returned in 'trim'
        self.CL=CL-1
        self.BL=BL-1
        self.LS_B=LS_B-1
        self.last_idx=last_idx
    def ConversionLine(self):
        for i in df.index:
            if self.CL <= i <= self.last_idx:
                max_value=max(max(df.loc[i-self.CL:i, 'Price']), max(df.loc[i-self.CL:i, 'Open']),\
                     max(df.loc[i-self.CL:i,'High']), max(df.loc[i-self.CL:i, 'Low']))
                min_value=min(min(df.loc[i-self.CL:i, 'Price']), min(df.loc[i-self.CL:i, 'Open']),\
                     min(df.loc[i-self.CL:i, 'High']), min(df.loc[i-self.CL:i, 'Low']))
                df.loc[i,'CL']=(max_value+min_value)/2
    def BaseLine(self):
        for i in df.index:
            if self.BL <= i <= self.last_idx:
                max_value=max(max(df.loc[i-self.BL:i, 'Price']), max(df.loc[i-self.BL:i, 'Open']),\
                     max(df.loc[i-self.BL:i, 'High']), max(df.loc[i-self.BL:i, 'Low']))
                min_value=min(min(df.loc[i-self.BL:i, 'Price']), min(df.loc[i-self.BL:i, 'Open']),\
                     min(df.loc[i-self.BL:i, 'High']), min(df.loc[i-self.BL:i, 'Low']))
                df.loc[i,'BL']=(max_value+min_value)/2
    def LeadingSpan_A(self): # Count 26-day including the start-day
        CL_dict={}
        for i in df.index:
            if self.CL <= i <= self.last_idx:
                max_value=max(max(df.loc[i-self.CL:i, 'Price']), max(df.loc[i-self.CL:i, 'Open']),\
                     max(df.loc[i-self.CL:i, 'High']), max(df.loc[i-self.CL:i, 'Low']))
                min_value=min(min(df.loc[i-self.CL:i, 'Price']), min(df.loc[i-self.CL:i, 'Open']),\
                     min(df.loc[i-self.CL:i, 'High']), min(df.loc[i-self.CL:i, 'Low']))
                CL_dict[i]=(max_value+min_value)/2
        BL_dict={}
        for i in df.index:
            if self.BL <= i <= self.last_idx:
                max_value=max(max(df.loc[i-self.BL:i, 'Price']), max(df.loc[i-self.BL:i, 'Open']),\
                     max(df.loc[i-self.BL:i, 'High']), max(df.loc[i-self.BL:i, 'Low']))
                min_value=min(min(df.loc[i-self.BL:i, 'Price']), min(df.loc[i-self.BL:i, 'Open']),\
                     min(df.loc[i-self.BL:i, 'High']), min(df.loc[i-self.BL:i, 'Low']))
                BL_dict[i]=(max_value+min_value)/2
        for i in df.index:
            if self.BL <= i <= self.last_idx:
                df.loc[i+25,'LS_A']=(CL_dict.get(i)+BL_dict.get(i))/2
    def LeadingSpan_B(self): # Count 26-day including the start-day
        for i in df.index:
            if self.LS_B <= i <= self.last_idx:
                max_value=max(max(df.loc[i-self.LS_B:i, 'Price']), max(df.loc[i-self.LS_B:i, 'Open']),\
                     max(df.loc[i-self.LS_B:i, 'High']), max(df.loc[i-self.LS_B:i, 'Low']))
                min_value=min(min(df.loc[i-self.LS_B:i, 'Price']), min(df.loc[i-self.LS_B:i, 'Open']),\
                     min(df.loc[i-self.LS_B:i, 'High']), min(df.loc[i-self.LS_B:i, 'Low']))
                df.loc[i+25, 'LS_B']=(max_value+min_value)/2

def BB_Band(period, n, last_idx): # period=20, n=2
    TP=[]
    for i in range(0, last_idx+1):
        tp=(df.loc[i,'High']+df.loc[i,'Low']+df.loc[i,'Price'])/3
        TP.append(tp)
    for i in range(0, last_idx+1):
        if i < (period-1):
            pass
        else: # Population Standard Deviation : pstdev
            df.loc[i,'BOLM']=mean(TP[i-(period-1):(i+1)])
            df.loc[i,'BOLU']=df.loc[i,'BOLM'] + pstdev(TP[i-(period-1):(i+1)])*n
            df.loc[i,'BOLD']=df.loc[i,'BOLM'] - pstdev(TP[i-(period-1):(i+1)])*n

def color_column(last_idx):
    red_start=[]
    blue_start=[]
    for idx in range(1, last_idx):
        if (df.loc[idx,"LS_B"] < df.loc[idx,"Open"] < df.loc[idx,"LS_A"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"Open"] < df.loc[idx,"LS_B"] < df.loc[idx,"LS_A"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"LS_B"] < df.loc[idx,"LS_A"] < df.loc[idx,"Open"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"LS_B"] < df.loc[idx,"LS_A"] < df.loc[idx,"Price"] < df.loc[idx,"Open"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"LS_A"] < df.loc[idx,"Open"] < df.loc[idx,"LS_B"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"Open"] < df.loc[idx,"LS_A"] < df.loc[idx,"LS_B"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"LS_A"] < df.loc[idx,"LS_B"] < df.loc[idx,"Open"] < df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"LS_A"] < df.loc[idx,"LS_B"] < df.loc[idx,"Price"] < df.loc[idx,"Open"] and\
            df.loc[idx-1,"Price"] <= df.loc[idx-1,"LS_B"]):
            red_start.append(idx)
        elif (df.loc[idx,"LS_A"] > df.loc[idx,"Open"] > df.loc[idx,"LS_B"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"Open"] > df.loc[idx,"LS_A"] > df.loc[idx,"LS_B"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"LS_A"] > df.loc[idx,"LS_B"] > df.loc[idx,"Open"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"LS_A"] > df.loc[idx,"LS_B"] > df.loc[idx,"Price"] > df.loc[idx,"Open"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_B"]) or\
            (df.loc[idx,"LS_B"] > df.loc[idx,"Open"] > df.loc[idx,"LS_A"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"Open"] > df.loc[idx,"LS_B"] > df.loc[idx,"LS_A"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"LS_B"] > df.loc[idx,"LS_A"] > df.loc[idx,"Open"] > df.loc[idx,"Price"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_A"]) or\
            (df.loc[idx,"LS_B"] > df.loc[idx,"LS_A"] > df.loc[idx,"Price"] > df.loc[idx,"Open"] and\
            df.loc[idx-1,"Price"] >= df.loc[idx-1,"LS_A"]):
            blue_start.append(idx)
    red_end=[]
    blue_end=[]
    # for "Red"
    for n in range(0, len(red_start)):
        for idx in range(1, last_idx):
            if df.loc[idx,'BOLU'] > df.loc[idx-1,'BOLU'] and df.loc[idx,'BOLU'] > df.loc[idx+1,'BOLU']:
                if red_start[n] <= idx:
                    red_end.append(idx)
                    break
                else:
                    continue
    if len(red_start) > len(red_end):
        for i in range(len(red_start)-len(red_end)):
            red_end.append(red_start[len(red_start)-1])
    # for "Blue"
    for n in range(0, len(blue_start)):
        for idx in range(1, last_idx):
            if df.loc[idx,'BOLD'] < df.loc[idx-1,'BOLD'] and df.loc[idx,'BOLD'] < df.loc[idx+1,'BOLD']:
                if blue_start[n] <= idx:
                    blue_end.append(idx)
                    break
                else:
                    continue
    if len(blue_start) > len(blue_end):
        for i in range(len(blue_start)-len(blue_end)):
            blue_end.append(blue_start[len(blue_start)-1])
    # print(red_start)
    # print(red_end)
    # print(blue_start)
    # print(blue_end)
    return red_start, red_end, blue_start, blue_end

def Remove_Overlaps(): 
    # when two columns in different colors are overlapped : the previous one is deleted ; turned into 'Zero'
    for r in range(0, len(red_start)):
        for b in range(0, len(blue_start)):
            # 1) (Blue Start)-(Red Start)-(Blue End)-(Red End) or (Red Start)-(Blue Start)-(Red End)-(Blue End)
            if red_start[r] < blue_end[b] < red_end[r]:
                blue_start[b]=0
                blue_end[b]=0
            elif blue_start[b] < red_end[r] < blue_end[b]:
                red_start[r]=0
                red_end[r]=0
            # 2) (Red and Blue Start)-(Red or Blue End)-(Blue or Red End)
            #     Blue Start & Red Start cannot happen simultaneously
            # 3) (Blue Start)-(Red Start)-(Red End)-(Blue End) or (Red Start)-(Blue Start)-(Blue End)-(Red End)
            # 4) (Blue Start)-(Red Start)-(Blue and Red End) or (Red Start)-(Blue Start)-(Red and Blue End)
            elif red_start[r] < blue_start[b] < blue_end[b] <= red_end[r]:
                red_start[r]=0
                red_end[r]=0
            elif blue_start[b] < red_start[r] < red_end[r] <= blue_end[b]:
                blue_start[b]=0
                blue_end[b]=0
            else:
                pass
    # when two columns in same color are overlapped : the later one is deleted ; turned into 'Zero'
    # when the color is red;
    for r1 in range(0, len(red_start)):
        for r2 in range(0, len(red_start)):
            # 1) (1_start)-(2_start)-(1_end)-(2_end)
            if r1<r2 and red_start[r2] < red_end[r1] < red_end[r2]:
                red_start[r2]=0
                red_end[r2]=0
            # 2) same start & different end => impossible
            # 3) (1_start)-(2_start)-(2_end)-(1_end)
            # 4) different start point & same end point
            elif r1<r2 and red_start[r1] < red_start[r2] < red_end[r2] <= red_end[r1]:
                red_start[r2]=0
                red_end[r2]=0
            else:
                pass
    # when the color is blue;
    for b1 in range(0, len(blue_start)):
        for b2 in range(0, len(blue_start)):
            # 1) (1_start)-(2_start)-(1_end)-(2_end)
            if b1<b2 and blue_start[b2] < blue_end[b1] < blue_end[b2]:
                blue_start[b2]=0
                blue_end[b2]=0
            # 2) same start & different end => impossible
            # 3) (1_start)-(2_start)-(2_end)-(1_end)
            # 4) different start point & same end point
            elif b1<b2 and blue_start[b1] < blue_start[b2] < blue_end[b2] <= blue_end[b1]:
                blue_start[b2]=0
                blue_end[b2]=0
            else:
                pass
    # when the 'start' and the 'end' are same so that it is not a column but a 'line', make'em into 'Zero'
    for i in range(0, len(red_start)):
        if red_start[i]==red_end[i]:
            red_start[i]=0
            red_end[i]=0
    for i in range(0, len(blue_start)):
        if blue_start[i]==blue_end[i]:
            blue_start[i]=0
            blue_end[i]=0
    # print(red_start)
    # print(red_end)
    # print(blue_start)
    # print(blue_end)
    RedNBlue=[red_start, red_end, blue_start, blue_end]  # remove the 'Zero's in each lists
    for i in range(0, len(RedNBlue)):
        cnt=0
        for j in range(0, len(RedNBlue[i])):
            if RedNBlue[i][j]==0:
                cnt+=1
        for k in range(0, cnt):
            RedNBlue[i].remove(0)
    # print(red_start)
    # print(red_end)
    # print(blue_start)
    # print(blue_end)

def fileType_xticks(file, last_idx):
    wb=openpyxl.load_workbook(file+'.xlsx')
    ws=wb.active
    if ws["A2"].number_format == 'General':
        plt.xticks([0, last_idx])
    else:
        pass


# DATA Processing
filename=input("=>  ")
file=filename   # (http://investing.com)
df = pd.read_excel(file+'.xlsx')
last_idx = trim(df)
for i in range(1, 26):
        df.loc[last_idx+i] = ['', '', '', '', '']

column_heads=['SMA-ML', 'SMA-UL', 'SMA-LL', 'LS_A', 'LS_B', 'BOLM', 'BOLU', 'BOLD']
for col in column_heads:
    df[col]=''
    df[col]=pd.to_numeric(df[col])

SMA_ATR(250, last_idx)
ichimoku=Ichimoku(9, 26, 52, last_idx)
ichimoku.LeadingSpan_A()
ichimoku.LeadingSpan_B()
BB_Band(20, 2, last_idx)
red_start, red_end, blue_start, blue_end = color_column(last_idx)
Remove_Overlaps()   

print(df)
df.to_excel('graph, '+file+'.xlsx')


# Visualization
plt.figure(figsize=(20, 10))

date=df['Date'][:last_idx+1]
plt.plot(date, df['Price'][:last_idx+1], label='Price', color='navy', lw=0.6)
plt.plot(date, df['SMA-ML'][:last_idx+1], label='SMA-ML', color='green', linestyle='--')
plt.plot(date, df['SMA-UL'][:last_idx+1], label='SMA-UL', color='red')
plt.plot(date, df['SMA-LL'][:last_idx+1], label='SMA-LL', color='blue')

LS_A=df['LS_A'][:last_idx+1]
LS_B=df['LS_B'][:last_idx+1]
plt.plot(date, LS_A, label='ICMK_LS_A', color='orange', lw=0.6)
plt.plot(date, LS_B, label='ICMK_LS_B', color='skyblue', lw=0.6)
plt.fill_between(date, LS_A, LS_B, where=(LS_A >= LS_B), color='orange', alpha=0.3, interpolate=True)
plt.fill_between(date, LS_A, LS_B, where=(LS_A < LS_B), color='skyblue', alpha=0.3, interpolate=True)

plt.plot(date, df['BOLM'][:last_idx+1], label='BB_M', color='green', ls="--", lw=0.4, alpha=0.6)
plt.plot(date, df['BOLU'][:last_idx+1], label='BB_U', color='red', lw=0.4, alpha=0.8)
plt.plot(date, df['BOLD'][:last_idx+1], label='BB_D', color='blue', lw=0.4, alpha=0.8)

for i in range(0, len(red_start)):
    plt.axvspan(date[red_start[i]], date[red_end[i]], alpha=0.3, color='red')
    plt.hlines(max(df.loc[red_start[i]:red_end[i], 'Price']), date[red_start[i]], date[red_end[i]], color='green', lw=0.7)
    plt.text(date[red_start[i]], max(df.loc[red_start[i]:red_end[i], 'Price']), max(df.loc[red_start[i]:red_end[i], 'Price']),\
             ha='left', fontsize=8, color='green', alpha=0.7)
for i in range(0, len(blue_start)):
    plt.axvspan(date[blue_start[i]], date[blue_end[i]], alpha=0.3, color='blue')
    plt.hlines(min(df.loc[blue_start[i]:blue_end[i], 'Price']), date[blue_start[i]], date[blue_end[i]], color='yellow', lw=0.7)
    plt.text(date[blue_start[i]], min(df.loc[blue_start[i]:blue_end[i], 'Price']), min(df.loc[blue_start[i]:blue_end[i], 'Price']),\
         ha='left', fontsize=8, color='yellow', alpha=0.7)

plt.title(f'{file}, for {last_idx+1}days', fontsize=20)
fileType_xticks(file, last_idx)
plt.grid(axis='y')
plt.legend()

plt.savefig('graph, '+file+'.png', dpi=150)