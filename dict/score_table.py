import pickle
with open ('O_code_6.pkl', 'rb') as f:
    O_code = pickle.load(f)

m = 6

values = list(O_code.values())
single_scores = {}
for value in values:
    for i in range(8):
        state = str(i) + value
        single_scores[state] = int(value[0]) + int(value[1]) * 3
single_scores

combine_scores = {}
for s1 in single_scores:
    for s2 in single_scores:
        if int(s1[0]) != int(s2[0]):
            # caculate the factor
            bias = 0
            i = int(s1[0])
            j = int(s2[0])
            # 45°
            if j - i == 1 or j-i == 7:
                factor = 1.5
            # 180°
            elif j-i == 4:
                if int(s1[1]) + int(s2[1]) >= m+1:
                    if int(s1[2]) + int(s2[2]) >= m-1:
                        bias = 1000
                factor = 2
            # 90°
            elif j-i == 2 or j-i == 6 :
                factor = 1.2
            # 135°   
            elif j-i ==3 or j-i == 5:
                factor = 1
            score = (single_scores[s1] + single_scores[s2]) * factor + bias
            state = s1+s2
            combine_scores[state] = round(score, 3)

with open ('6.pkl','wb') as f:
    pickle.dump(combine_scores,f)

print(single_scores)
#print(combine_scores['011441']) 