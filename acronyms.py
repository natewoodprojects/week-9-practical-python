acronyms = ["SMH"]

acronyms.append('LOL')
acronyms.append('IDK')
acronyms.append('BFN')
acronyms.append('IMHO')

del acronyms[4]
acronyms.remove("IDK")


if "LOL" in acronyms: 
    print("YUP! It's here!")

print(acronyms)

for acronym in acronyms: 
    print(acronym)
    