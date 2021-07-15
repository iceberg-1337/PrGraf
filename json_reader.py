import json

def jsonIN():


    with open('logger.txt', 'r', encoding="utf-8") as f:
        data = json.load(f)


    x_arr = []
    y_arr = []
    x = 0


    for item in data:
        if data[item]["uName"] == "Тест Студии":
            x_arr.append(x)
            y_arr.append(data[item]["data"]["BME280_temp"])
            x+=1

    return (x_arr, y_arr)

'''print(y_arr)
print(x_arr)
max_temp = max(y_arr)
min_temp = min(y_arr)


print(min_temp)
print(max_temp)'''