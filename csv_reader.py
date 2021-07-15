import csv

def csvIN():
      x_arr = []
        y_arr = []
        x = 0

    file_name = 'last_export.csv'

    with open(file_name, 'r', encoding='cp1251') as f_obj:
        line = f_obj.readline()
        reader = csv.DictReader(f_obj, delimiter=';')


      


        for line in reader:
            arr_x.append(x)
            arr_y.append((line['BMP280_temp']))
            x += 1

    return (x_arr, y_arr)