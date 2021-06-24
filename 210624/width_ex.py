
# 퀴즈

for x in range(1, 51):
    title = str(x)+"주차.txt"
    with open(title, "w", encoding="utf8") as report_file:
        # report_file.write("- " + str(x)+" 주차 주간보고 -\n")
        # report_file.write("부서 : \n")
        # report_file.write("이름 : \n")
        # report_file.write("업무요약 : \n")

        report_file.write("- {0} 주차 주간보고 -".format(x))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")
    