import os

file_names = []

def search_file_names():
    file_path = ".\\"
    for i,j,k in os.walk(file_path):
        if len(k) > 0:
            for file_name in k:
                if file_name[-4:] == ".txt":
                    file_names.append(i + "\\" + file_name)

def main():
    for file_name in file_names:
        file_obj = open(file_name, "r", encoding="ISO-8859-15")
        file_content = file_obj.read()
        file_content = "保存时间" + file_content
        file_content = file_content.split("保存时间")
        file_obj.close()
        file_obj = open(file_name, "w", encoding="ISO-8859-15")
        file_obj.write(file_content[-1])
        file_obj.close()
        print(file_name + " done")

if __name__ == "__main__":
    search_file_names()
    main()