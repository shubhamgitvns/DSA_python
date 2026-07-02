from operator import itemgetter


# list=["Happy Birthday Prince","India v England","India v England"," Happy Birthday Prince","Happy Birthday Prince",
# "India v England","Happy Birthday Prince","Summer","Summer","Summer","Happy Birthday Prince"]
# frq = {}
# for i in list:
#     frq[i] = list.count(i)

# top3 = sorted(frq.items(), key=itemgetter(1), reverse=True)    
# for key, value in top3[:3]:
#     print(key,"-",value)



frq ={}

while True:
    data = input("Enter: ")
    
    if data == 'exit':
        break
    if data in frq:
        frq[data] += 1
    else:
        frq[data] =1
    for key, value in frq.items():
       print(key,"-",value)

