import os

file_names = set()

def search_file_names():
    file_path = "D:\\Temp_data"
    for i,j,k in os.walk(file_path):
        #print(i,j,k)
        if len(k) > 0:
            for file_name in k:
                if file_name[-4:] == ".txt":
                    file_names.add(i + "\\" + file_name)


def main():
    #file_names.add("D:\\Temp_data\\20180527\\20180527-69.txt")
    for file_name in file_names:
        try:
            file_obj = open(file_name, "r", encoding="GBK")
            flag = "GBK"
            file_content = file_obj.read()
        except:
            try:
                file_obj.close()
            except:
                pass
            file_obj = open(file_name, "r", encoding="ISO-8859-15")
            flag = "ISO-8859-15"
            file_content = file_obj.read()
        
        file_content = "保存时间" + file_content
        file_content = file_content.split("保存时间")
        file_obj.close()
        if flag == "GBK":
            file_obj = open(file_name, "w", encoding="GBK")
        else:
            file_obj = open(file_name, "w", encoding="ISO-8859-15")
        file_obj.write(file_content[-1])
        file_obj.close()
        print(file_name + " done")

if __name__ == "__main__":
    search_file_names()
    #print(len(file_names))
    #print(file_names)
    main()