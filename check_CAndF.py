import os
import re

# 存储类和函数定义的位置
definitions = {}


def find_classes_and_functions(directory):
    # 正则表达式匹配类和函数定义
    class_pattern = re.compile(r'^\s*class\s+(\w+)\s*\(.*\):')
    function_pattern = re.compile(r'^\s*def\s+(\w+)\s*\(.*\):')

    # 遍历文件夹及其子文件夹中的所有 .py 文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

                print(f"\nIn file: {relative_path}")

                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        # 检查类定义
                        class_match = class_pattern.match(line)
                        if class_match:
                            class_name = class_match.group(1)
                            print(f"Found class: {class_name}")
                            # 将类名和对应的文件存储到字典中
                            if class_name not in definitions:
                                definitions[class_name] = []
                            definitions[class_name].append(relative_path)

                        # 检查函数定义
                        function_match = function_pattern.match(line)
                        if function_match:
                            function_name = function_match.group(1)
                            print(f"Found function: {function_name}")
                            # 将函数名和对应的文件存储到字典中
                            if function_name not in definitions:
                                definitions[function_name] = []
                            definitions[function_name].append(relative_path)


def search_class_or_function():
    while True:
        # 用户输入类或函数名
        search_name = input("\nEnter the class or function name to search for (or '##' to exit): ")

        # 检查是否需要退出程序
        if search_name == "##":
            print("Exiting the search.")
            break

        # 检查输入的类或函数是否在定义中
        if search_name in definitions:
            print(f"\n{search_name} is found in the following files:")
            for file_path in definitions[search_name]:
                print(f"  - {file_path}")
        else:
            print(f"\n{search_name} not found in any .py files.")


if __name__ == "__main__":
    # 获取用户输入的文件夹路径
    directory = input("Please enter the directory to search for .py files: ")

    # 检查输入的路径是否存在
    if os.path.isdir(directory):
        # 查找所有类和函数
        find_classes_and_functions(directory)

        # 用户输入要搜索的类或函数，循环查找直到输入 '##' 退出
        search_class_or_function()
    else:
        print("The directory does not exist. Please enter a valid directory.")

