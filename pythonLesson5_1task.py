#Напишите программу, удаляющую из текста все слова, содержащие ""абв""

str = "Я люблю джваабв иабв Питон!"

# def delete(_string):
#     result = []
#     data = _string.split()
#     for i in data:        
#         if "абв" not in i:           
#             result.append("" + i)
#     return result 

# def delete(_string):
#     str = _string.split()
#     result =[i for i in str if "абв" not in i ]
#     return result

# print(*delete(str))

result = list(filter(lambda string:"абв" not in string, str.split()))
print(*result)


            
            