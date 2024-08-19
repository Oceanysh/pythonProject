import re


def extract_log_entries(input_file, output_file, keyword):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
            open(output_file, 'w', encoding='utf-8') as outfile:

        in_entry = False
        current_entry = []

        for line in infile:
            if keyword in line:
                if in_entry:
                    # 写入前一个条目（如果有）
                    outfile.write(''.join(current_entry))
                    current_entry = []
                in_entry = True

            if in_entry:
                current_entry.append(line)

            # 检查是否为日志条目的结束
            if in_entry and re.match(r'^\d{4}-\d{2}-\d{2}', line):
                if current_entry:
                    outfile.write(''.join(current_entry))
                    current_entry = []
                in_entry = False

        # 写入最后一个条目（如果有）
        if current_entry:
            outfile.write(''.join(current_entry))


# 使用示例
input_file = '/Users/shy/PycharmProjects/split_log_ae'  # 替换为实际的日志文件路径
output_file = 'extracted_logs.txt'  # 输出文件名
keyword = 'A000472490'

extract_log_entries(input_file, output_file, keyword)
print(f"提取的日志条目已保存到 {output_file}")