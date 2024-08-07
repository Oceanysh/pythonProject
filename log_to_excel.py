import re
import pandas as pd
from datetime import datetime
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def parse_log_line(line):
    # 解析日志行
    timestamp_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})', line)
    if not timestamp_match:
        return None

    timestamp = timestamp_match.group(1)

    # 提取关键信息
    info = {
        'timestamp': timestamp,
        'type': 'Unknown',
        'details': ''
    }

    if 'queryFix Request' in line:
        info['type'] = 'Request'
        request_match = re.search(r'queryFix Request=(.*)', line)
        if request_match:
            info['details'] = request_match.group(1)

    elif 'queryFix Response' in line:
        info['type'] = 'Response'
        response_match = re.search(r'queryFix Response=(.*)', line)
        if response_match:
            info['details'] = response_match.group(1)

    elif '[扫描线程]' in line:
        info['type'] = 'Scan'
        info['details'] = line.split('[扫描线程]')[1].strip()

    elif '短信所属营业' in line:
        info['type'] = 'SMS'
        info['details'] = line.split('短信所属营业：')[1].strip()

    return info


def process_log_file(file_path):
    data = []
    encoding = detect_encoding(file_path)
    print(f"检测到的文件编码: {encoding}")

    with open(file_path, 'r', encoding=encoding, errors='replace') as file:
        for line in file:
            parsed_info = parse_log_line(line)
            if parsed_info:
                data.append(parsed_info)
    return data


def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)


# 使用示例
log_file_path = '/Users/shy/DingDian/zxzq/log.log.2024-07-22'
output_excel_file = '/Users/shy/DingDian/zxzq/output_log_analysis.xlsx'

log_data = process_log_file(log_file_path)
save_to_excel(log_data, output_excel_file)

print(f"日志分析完成，结果已保存到 {output_excel_file}")