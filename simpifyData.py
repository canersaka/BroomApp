file = open("test.csv", "a")
import csv
with open('BostonData.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        file.write("\"" + ",".join(row).replace(":","\":") + ",\n")
file.close()
# for a in open("data.csv"):
#     details = a.split(",")
#     if details[5] == "":
#         details[5] == "-1"
#     if not details[28] == "":
#         file.write(details[3] + "," + details[4] + "," + details[5] + "," + details[6] + "," + details[7] + "," + details[28])
#         file.write("\n")