pathInput = "./pythonLesson5_4task/input.txt"
pathOutput = "./pythonLesson5_4task/Output.txt"



with open(pathInput, "r") as read:
  data = read.readline()


def rleCoding(data):
  count = 1; 
  result = []
  for symbol in range(len(data)):   
    if len(data)-1 == symbol:    
      result.append(str(count))  
      result.append(data[symbol])
      return "".join(result)
    else:  
      if data[symbol] == data[symbol+1]:    
        count += 1   
      else: 
        if count != 1:
          result.append(str(count))  
          result.append(data[symbol])
          count = 1; 
        else:
          result.append(data[symbol])      
  return "".join(result)

def rleDecoded(str):
  resulst = []
  for i in range(len(str)):
    if str[i].isdigit():
      count = int(str[i])
      for _ in range(count-1):
       resulst.append(str[i+1]) 
    else:
      resulst.append(str[i])  
  return "".join(resulst)


codingStr = rleCoding(data)
print(codingStr)
print(rleDecoded(codingStr))

with open(pathOutput, "w") as writer:
  writer.write(rleDecoded(codingStr))








 
