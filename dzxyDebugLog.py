import re
import pandas as pd


def process_log_file(file_path):
    synthesis_times = []
    ca_times = []

    with open(file_path, 'r') as file:
        for line in file:
            # 匹配合成耗时
            synthesis_match = re.search(r'异步PDF合成线程\d+：结束作业.*耗时:(\d+)', line)
            if synthesis_match:
                synthesis_times.append(int(synthesis_match.group(1)))

            # 匹配CA耗时
            ca_match = re.search(r'对接CA耗时(\d+)', line)
            if ca_match:
                ca_times.append(int(ca_match.group(1)))

    return synthesis_times, ca_times


def create_excel(synthesis_times, ca_times, output_file):
    df = pd.DataFrame({
        '合成耗时': synthesis_times,
        'CA耗时': ca_times
    })

    # 计算平均值
    averages = df.mean()

    # 创建一个新的DataFrame来存储平均值
    avg_df = pd.DataFrame({
        '统计项': ['合成耗时平均值', 'CA耗时平均值'],
        '平均值 (毫秒)': [averages['合成耗时'], averages['CA耗时']]
    })

    # 创建ExcelWriter对象
    with pd.ExcelWriter(output_file) as writer:
        df.to_excel(writer, sheet_name='原始数据', index=False)
        avg_df.to_excel(writer, sheet_name='平均值统计', index=False)


def main():
    log_file = '/Users/shy/DingDian/zxzq/需求/非现场/2024/资产账户扩展限制增加/debug.log'  # 替换为实际的日志文件路径
    output_file = 'statistics.xlsx'

    synthesis_times, ca_times = process_log_file(log_file)
    create_excel(synthesis_times, ca_times, output_file)
    print(f"统计结果已保存到 {output_file}")


if __name__ == "__main__":
    main()