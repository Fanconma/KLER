import os
import json

def replace_lines_from_file(map_file_path, input_file):
    # 加载之前保存的 line_map
    with open(map_file_path, 'r', encoding='utf-8') as map_file:
        line_map = json.load(map_file)
    
    new_line_map = {}
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        for line in lines:
            parts = line.split('||', 2)
            if len(parts) < 3:
                print(f"Skipping invalid line in input file: {line}")
                continue
            file_path, idx_str, content = parts
            try:
                idx = int(idx_str)
            except ValueError:
                print(f"Invalid line number '{idx_str}' in line: {line}")
                continue

            if file_path not in new_line_map:
                new_line_map[file_path] = []
            new_line_map[file_path].append((idx, content.strip()))
        
        for file_path, replacements in new_line_map.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_lines = file.readlines()
                
                for idx, new_line in replacements:
                    file_lines[idx] = new_line + '\n'
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(file_lines)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    except Exception as e:
        print(f"Error reading input file {input_file}: {e}")

# 示例用法
input_file = 'path/to/output_file.txt'  # 替换为你的输出文件路径
map_file_path = 'path/to/line_map.json'  # 替换为你的line_map文件路径

# 将修改后的内容返回到原文件
replace_lines_from_file(map_file_path, input_file)
