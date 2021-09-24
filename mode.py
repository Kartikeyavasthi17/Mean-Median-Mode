import csv
from collections import Counter

with open('data2.csv',newline='') as f:
    reader=csv.reader(f)
    m_data=list(reader)
    m_data.pop(0)
    m_data.pop(1)
    
    new_data=[]
    for i in range(len(m_data)):
        l_num=m_data[i][2]
        new_data.append(float(l_num))

    n=len(new_data)
    all=0
    for weight in new_data:
        all +=weight

    mean=all/n

    new_data.sort()
    if n%2 == 0 :
        median=float(new_data[n//2])
        median2=float(new_data[n//2-1])
        Verifiedmedian=(median+median2)/2
    else :
        Verifiedmedian=new_data[n//2]
	

	#Calculating Mode
	data = Counter(new_data)
	mode_data_for_range = {
       "50-60": 0,
       "60-70": 0,
        "70-80": 0
	}
    
	for height, occurence in data.items():
	    if 50 < float(height) < 60:
	        mode_data_for_range["50-60"] += occurence
	    elif 60 < float(height) < 70:
	        mode_data_for_range["60-70"] += occurence
	    elif 70 < float(height) < 80:
	        mode_data_for_range["70-80"] += occurence
	

	mode_range, mode_occurence = 0, 0
	for range, occurence in mode_data_for_range.items():
	    if occurence > mode_occurence:
	        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
	mode = float((mode_range[0] + mode_range[1]) / 2)
	print(f"Mode is -> {mode:2f}")



    print("Mean/average is :",str(mean))
    print("Median is :",str(Verifiedmedian))