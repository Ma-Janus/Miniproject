import os
import shutil


def organize_files(directory):
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在，请检查路径后重试。")
        return

    # 遍历给定目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 检查是否为文件
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1]
            target_folder = os.path.join(directory, extension)

            # 如果目标文件夹不存在，则创建它
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 移动文件到对应的文件夹
            shutil.move(file_path, target_folder)
            print(f"Moved {filename} to {target_folder}")


# 示例调用
organize_files(r"C:\Users\Janus\Downloads")  # 更新为你自己的路径