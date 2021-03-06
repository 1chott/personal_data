import os

def main():
    # 输入原文件件
    src_dir = input("请输入需要拷贝的文件夹：")

    dst_dir = "[bk]" + src_dir #目的文件夹

    # 创建目的文件夹
    try:
        os.mkdir(dst_dir)
        print("创建%s成功"%("[bk] " + src_dir))
    except Exception as ret:
        print("创建文件夹失败：ret = ", ret)

    # 打开源文件夹，返回文件夹里面的内容，以列表方式返回
    filename_list = os.listdir(src_dir)
    # print(filename_list)

    # 遍历打印每一个文件的名字
    for filename in filename_list:
        src_path = src_dir + "/" + filename
        dst_path = dst_dir + "/" + filename
        print(src_path, " >> ", dst_path)

        #打开源文件内容，读取内容，把读取的内容写入到目的文件
        with open(src_path, "rb") as f1:
            content = f1.read()
            with open(dst_path, "wb") as f2:
                f2.write(content)




if __name__ == '__main__':
    main()