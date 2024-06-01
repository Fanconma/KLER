import os
import json

def search_and_extract_lines(directory, keyword, output_file, map_file):
    line_map = {}  # 用于存储每个文件中匹配的行
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        lines = infile.readlines()
                        matched_lines = []
                        for idx, line in enumerate(lines):
                            if keyword in line:
                                matched_lines.append((idx, line.strip()))
                                outfile.write(f"{file_path}||{idx}||{line}")
                        if matched_lines:
                            line_map[file_path] = matched_lines
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    # 将 line_map 保存到 map_file
    with open(map_file, 'w', encoding='utf-8') as map_file:
        json.dump(line_map, map_file)

# 示例用法
directory = 'path/to/your/directory'  # 替换为你的目录路径
keyword = 'KEYWORD'              # 替换为你要搜索的关键词
output_file = 'path/to/output_file.txt'  # 替换为你的输出文件路径
map_file = 'path/to/line_map.json'  # 替换为你的 line_map 文件路径

# 搜索并提取匹配的行
search_and_extract_lines(directory, keyword, output_file, map_file)
