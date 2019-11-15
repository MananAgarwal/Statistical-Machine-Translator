import sys
import numpy as np
import fileinput, string, sys, re
import math
from statistics import mean 

def preprocess(input_file):
    input_file = re.sub('[.,)(?"“”:;!]', r'', input_file, flags = re.M)
    input_file = re.sub("’s ", r' ', input_file, flags = re.M)
    input_file = re.sub("'s ", r' ', input_file, flags = re.M)
    input_file = re.sub("' s ", r' ', input_file, flags = re.M)
    input_file = re.sub(" – ", r' ', input_file, flags = re.M)
    input_file = re.sub("– ", r'', input_file, flags = re.M)
    input_file = re.sub("- ", r'', input_file, flags = re.M)
    input_file = re.sub(" -", r'', input_file, flags = re.M)
    input_file = re.sub("['’]", r'', input_file, flags = re.M)
    input_file = re.sub("[a-z-0-9]*/[a-z-0-9]*", r'', input_file, flags = re.M)
    input_file = re.sub("[A-Z]*[0-9]", r'', input_file, flags = re.M)
    input_file = re.sub("[0-9]", r'', input_file, flags = re.M)
    input_file = re.sub("  [ ]*", r' ', input_file, flags = re.M)
    input_file = re.sub("\n", r' ', input_file, flags = re.M) #IF WHOLE DOC
    return input_file

def cosine_similarity(v1, v2):
    a1 = np.asarray(v1)
    a2 = np.asarray(v2)
    mag_a1 = np.dot(a1,a1)
    mag_a2 = np.dot(a2,a2)
    sim = np.dot(a1,a2)/(np.sqrt(mag_a1)*np.sqrt(mag_a2))
    return sim

def cos(s1,s2):
    l = set(s1).union(set(s2))
#     print(l)
    d1 = {}
    d2 = {}
    for e in l:
        d1[e] = 0
        d2[e] = 0
    for w in s1:
        d1[w]+=1;
    for w in s2:
        d2[w]+=1;

    for w in d1.keys():
        if d1[w]==0:
            d1[w] = 1
        else:     
            d1[w] = (1 + math.log10(d1[w]))
    for w in d2.keys():
        if d2[w]==0:
            d2[w] = 1
        else:
            d2[w] = (1 + math.log10(d2[w]))
#     print(list(d1.values()))
#     print(list(d2.values()))
    return cosine_similarity(list(d1.values()), list(d2.values()))

def jaccard_correlation(s1,s2):
    count_intersection=0
    l = set(s1).union(set(s2))
#     print(l)
    d1 = {}
    d2 = {}
    for e in l:
        d1[e] = 0
        d2[e] = 0
    for w in s1:
        d1[w]+=1;
    for w in s2:
        d2[w]+=1;
    for e in l:
        count_intersection+=min(d1[e],d2[e]);
    sim=count_intersection/(len(s1)+len(s2)-count_intersection)
    return sim


print("Static transator")
print("Enter choice")
print("1-Dutch to English\n")
print("2-English to Dutch\n")
print("3-exit()\n")

choice=int(input())
first=""
second=""

if(choice==1):
    weights_file = "Trained_Model/dut_to_eng_100k_processed.npy"
    first=input("\nFile to be transalted\n")
    second=input("\nConverted File to test against\n")
elif(choice==2):
    weights_file = "Trained_Model/eng_to_dut_100k_processed.npy"
    first=input("\nFile to be transalted\n")
    second=input("\nConverted File to test against\n")
else:
    print("Exiting the code")			
    exit()

# weights_file = sys.argv[1]
# our_file_name = sys.argv[2]
our_file_name = first
# correct_file_name = sys.argv[3]
correct_file_name = second

## Open and Preprocess the files
our_file = open(our_file_name).read()
correct_file = open(correct_file_name).read()

our_file = preprocess(our_file)
correct_file = preprocess(correct_file)

# print(our_file)
# print(correct_file)

#Load the weights to all the pairs
t = np.load(weights_file, allow_pickle='TRUE').item()

#Assuming t is of the form ('english','dutch')
print("\nNo. of foreign/english pairs:",len(t))

convert = {}
conv_prob = {}

for pair in t.keys():
    if not isinstance(pair, tuple): #To make the code compatible with the preprocessed t outputs
        convert = t
        break
    if pair[1] not in conv_prob.keys():
        conv_prob[pair[1]] = 0
    if(conv_prob[pair[1]] < t[pair]):
        conv_prob[pair[1]] = t[pair]
        convert[pair[1]] = pair[0]

inverted_list = convert

##################### ON WHOLE DOC #####################
test = our_file
test_words = test.split(" ")

conv = []
for dw in test_words:
    if dw in inverted_list.keys():
        conv.append(inverted_list[dw])
# print(len(conv))

cor = correct_file
cor = cor.split(" ")
# print(len(cor))

cos_sim = cos(cor,conv)
jc_sim = jaccard_correlation(cor,conv)
print("Cosine Similarity: ", cos_sim)
print("Jaccard Coefficient: ", jc_sim)
##########################################################

##################### ON SENTENCE PAIRS ##################
# # Testing
# our_file = our_file.split('\n')
# correct_file = correct_file.split('\n')

# arr_cos = []
# arr_jc = []

# for i in range(len(our_file)):
# #     test = "De begrotingsruimte van de nationale lidstaten ligt politiek immers minder gevoelig"
#     test = our_file[i]
#     test_words = test.split(" ")
#     conv = []
#     for dw in test_words:
#         if dw in inverted_list.keys():
#             # conv =  conv + inverted_list[dw]
#             conv.append(inverted_list[dw]) #for manan
#     # print(conv)
    
# #     cor = "After all the scope of the budget of the national Member States is politically speaking less of a sensitive issue"
#     cor = correct_file[i]
#     cor = cor.split(" ")
#     # print(cor)
    
#     cos_sim = cos(cor,conv)
#     jc_sim = jaccard_correlation(cor,conv)
#     arr_cos.append(cos_sim)
#     arr_jc.append(jc_sim)
#     # print("Cosine Similarity: ", cos_sim)
#     # print("Jaccard Similarity: ", jc_sim)
#     # print()

# print()
# print("Average Cosine Similarity",mean(arr_cos))
# print("Average Jaccard Similarity",mean(arr_jc))
# #######################################################

# np.save('eng_to_dut_50k_processed.npy',inverted_list)