def fonk(list,list2):

    for i in list2:
        print(i)
        s = 0
        for j in i:
            s = s + 1
        print(s)

    ayırma = list.split(" ")

    print(ayırma)

list = "Uzak bir ormanda, birbirinden farklı hayvanların huzur içinde yaşadığı güzel bir yer vardı. Orman, meyve ağaçları, berrak dereleri ve rengârenk çiçekleriyle adeta bir cennetti. Bu ormanda Minik adında cesur bir karınca yaşardı."

list2 = ["emo","sadık","memet"]

print(fonk(list,list2))