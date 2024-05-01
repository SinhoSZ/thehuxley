ano = int(input())
periodo = input().lower()

if periodo == "dc" and ano >= 1790:
    print("IDADE CONTEMPORANEA")
elif periodo == "dc" and ano >= 1454:
    print("IDADE MODERNA")
elif periodo == "dc" and ano >= 477:
    print("IDADE MEDIA")
elif periodo == "ac" and ano >= 4000:
    print("PRE-HISTORIA")
else:
    print("ANTIGUIDADE") # Antiguidade = 4001 aC até 476 dC