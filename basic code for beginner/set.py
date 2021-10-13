s = set()
"""s_from_dict = set({"rony":"coder","ranjan":"developer"})
print(s_from_dict)
print(type(s_from_dict))"""
s.add(1)
s.add(4)
s1 = s.isdisjoint({1,2,3})
print(s,s1)