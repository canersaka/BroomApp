import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Fr33Burm@",
    database = "housingschema"
)

mycursor = mydb.cursor()

# sql = "INSERT INTO addsqm (houseNum, streetName, aprtNum, townName, zipCode, sqftArea) VALUES (%s,%s,%s,%s,%s,%s)"
# # val = (104,"PUTNAM ST","","EAST BOSTON","02128",2202)
# splitArr = [i.split(",") for i in open("BostonData.csv").read().split("\n")]
# arr = []
# for i,iv in enumerate(splitArr):
#     if iv[0] == "":
#         continue
#     if iv[2] == "-1":
#         iv[2] = ""
#     iv = iv[:-1] + iv[-1].split(":")
#     while(len(iv) != 6):
#         print(iv)
#         iv = iv[0:2] + [iv[2] + "," + iv[3]] + iv[4:]
#         print(iv)
#         print()
#     #print(iv)
#     iv[-1] = int(float(iv[-1]))
#     iv[0] = int(iv[0])
#     arr += [tuple(iv)]
# #print(arr)

# mycursor.executemany(sql,arr)
# mydb.commit()
# print(mycursor.rowcount)
# # mycursor.execute("SHOW TABLES")
# # for i in mycursor:
# #     print(i)



# mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM addsqm WHERE ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


