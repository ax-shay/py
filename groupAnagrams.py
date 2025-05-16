from collections import defaultdict
class Solution:
   def groupAnagrams(self, strs):
      # create a target dictionary to store result
      res_dict = defaultdict(list)

      # Iterate thru list elements
      for elem in strs:
         lst = [0] * 26
         for i in range(len(elem)):
            lst[ord(elem[i]) - ord('a')] += 1
         
         # For-each List element, get the signature value and store in dict as elem:signature (infact, 'signature':[elem])
         # res_dict[elem] = lst
         res_dict[str(lst)].append(elem)
      print('res_dict is :: ', res_dict)
      
      # run thru the dict to gather elems with similar values
      # final_dict = defaultdict(list)
      # for k, v in res_dict.items():
      #    final_dict[(str(v))].append(k)
      # print(final_dict)

      # return list of list
      return list(res_dict.values())

s = Solution()
print(s.groupAnagrams(['', '', '']))