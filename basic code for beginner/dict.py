d1={"Rony":"coder","Ranjan":"Developer","Harry":"UI&UX"}
d1["jinal"]="Ncc"
d1["Saim"]="Nss"
del d1["Saim"]
d3 = d1.copy()
del d3["Harry"]
d1.update({"Sefali":"Pizza"})
print(d1.keys())
print(d1.items())
print(d1)
print(d3)
print(type(d1))