import sys

import pandas as pd
import numpy as np
import csv
from serial import Serial
import time


# file1 = open("../txt_files/eggdata.txt","r+")
# file2 = open("../txt_files/cornflakes.txt","r+")
# data=file1.readlines()
# data2=file2.readlines()

# del data[-1]
# del data[0]
# del data2[-1]
# del data2[0:2]t


##collects bytes of serial data from the stm32 nucleo and stores them in 2D list

# def serial_fsr_collect(desired_number_rows):
#     data_one = ""
#     data_two = ""
#
#     start_time = time.time()
#     elapsed_time = time.time() - start_time
#
#     ser = Serial('COM5', 9600, timeout=1)  ##/dev/ttyACM0 for linux
#     ser.flushInput()
#     str_buff = ""
#     count = 0
#     data_one_list = []
#     row_count = 0
#
#     ## add 4 because we scrap the first row and last to not have to omit garbage data, plus two others that have double commas
#     while row_count < desired_number_rows + 4:
#         ser_byte = ser.read()
#         # print(ser_byte)
#
#         if not ser_byte == b' ':
#             buff = int(ser_byte)
#             str_buff += str(buff)
#         if count == 160:
#             # if data_one[-1] ==',':
#             #     data_one = data_one[0:-1]
#             # if data_one[0]==',':
#             #     data_one = data_one[1:]
#             # data_one+='\n'
#             data_one_list.append(data_one.split(","))
#             count = 0
#             data_one = ""
#             row_count += 1
#             print(row_count)
#         if ser_byte == b' ':
#             count += 1
#             data_one = data_one + str_buff + ','
#             str_buff = ""
#
#         elapsed_time = time.time() - start_time
#         # print (elapsed_time)
#
#     # print(data_one_list)
#
#     # delete first row because it is garbage
#     del data_one_list[0]
#     # delete the last row, because it will often not be full in length
#     del data_one_list[-1]
#
#     # search for any rows with a double comma and delete them
#     for i in range(len(data_one_list)):
#         # minus one to not go out index range at the end of the row
#         for j in range(len(data_one_list[i]) - 1):
#             if data_one_list[i][j] == ',' and data_one_list[i][j + 1] == ',':
#                 del data_one_list[i]
#                 break
#
#     del data_one_list[0]
#     del data_one_list[1]
#
#     # print("\n")
#     # print("\n")
#     # print("\n")
#     # print("\n")
#     # print("\n")
#     # print("\n")
#     # print(data_one_list)
#     return data_one_list

def open_serial_connection():
    # COM ports are managed differently based on OS
    if sys.platform.startswith('linux'):
        return Serial('/dev/ttyACM0', 115200, timeout=1)
    elif sys.platform.startswith('win'):
        return Serial('COM5', 115200, timeout=1)
    else:
        raise EnvironmentError(sys.platform + ' is an unsupported platform')


def collect_reading(ser):
    line = ser.readline().strip()
    reading = [int(x) for x in line.decode().split()]  # convert reading to 1D numpy array
    if len(reading) != 160:
        return False
    return reading


def serial_fsr_collect(num_readings):
    ser = open_serial_connection()
    ser.flushInput()
    ser.readline()  # omit garbage row
    out_arr = []
    try:
        for i in range(num_readings):  # read num_readings inputs from the FSR matrix and return them as 2d array
            reading = collect_reading(ser)
            if not reading:
                print("row", i, "failed")
                continue
            out_arr.append(reading)
            print(i, "out of", 10000)

    except ValueError:
        print("The serial connection did not completely transfer the readings. Try replugging the serial connection.")

    return np.asarray(out_arr)


# this function is meant to be used by the tensorflow_pipeline2 file, should move eventually
def clean_list():
    data_list = serial_fsr_collect(20)
    pd_ob = pd.DataFrame(data_list)
    pd_ob.drop(pd_ob.columns[len(pd_ob.columns) - 1], axis=1, inplace=True)
    pd_ob = pd_ob.apply(pd.to_numeric)
    readable_list = pd_ob.values.tolist()

    # print(readable_list)
    return readable_list


if __name__ == '__main__':

    object_type = input("Enter an object type (wcu: wooden cube, wc:wood cylinder, fs: foam sphere, n: nothing: ")
    data_one_list = serial_fsr_collect(10000)
    pd_ob = pd.DataFrame(data_one_list)
    # pd_ob.drop(pd_ob.columns[len(pd_ob.columns) - 1], axis=1, inplace=True)

    print(pd_ob)

    if input("save this data? (y/N)").lower() in ["yes", "y"]:
        if object_type == 'wc':
            pd_ob["label"] = 3
            export_csv = pd_ob.to_csv('export_dataframe_wood_cylinder.csv', index=None,
                                      header=True)  # Don't forget to add '.csv' at the end of the path

        if object_type == 'wcu':
            pd_ob["label"] = 2

            export_csv = pd_ob.to_csv('export_dataframe_wood_cube.csv', index=None,
                                      header=True)  # Don't forget to add '.csv' at the end of the path

        elif object_type == "fs":
            pd_ob["label"] = 1
            export_csv = pd_ob.to_csv('export_dataframe_foam_sphere.csv', index=None,
                                      header=True)  # Don't forget to add '.csv' at the end of the path

        elif object_type == "n":
            pd_ob["label"] = 0
            export_csv = pd_ob.to_csv('export_dataframe_nothing.csv', index=None,
                                      header=True)  # Don't forget to add '.csv' at the end of the path
        print("data saved")
