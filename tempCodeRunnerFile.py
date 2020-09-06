#     for one_comb in comb:
#         for i in one_comb:
#             binary = bin(i)[2:]
#             if i != max_num:
#                 zero_cnt += binary.count('0') + (max_bin - len(binary))
#             else:
#                 zero_cnt += binary.count('0')
                
#             one_cnt += binary.count('1')
            
#     if one_cnt == zero_cnt:
#         tot_cnt += 1
#         bin_tot = '0'*(max_bin - len(bin(tot_cnt)[2:])) + str(bin(tot_cnt)[2:])
#         zero_cnt, one_cnt = 0,0
        
# print(bin_tot,end="")
import collections
def pset(seqqq):
    if len(seqqq) <= 1: