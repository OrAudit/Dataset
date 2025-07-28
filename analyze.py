"""
Use slither to analyze the contract source code according to the contract address on Ethereum.
"""
import subprocess
import pandas as pd
from tqdm import tqdm

INDEX = 0
df = pd.read_csv('chainlink/feed/AggregatorV3Interface/contracts.csv')
contract_addresses = df['Address'].dropna().tolist()
addresses_to_analyze = contract_addresses[INDEX:]
tqdm_bar = tqdm(addresses_to_analyze, initial=INDEX, total=len(contract_addresses),
                desc="Analyzing contracts", unit="contract")

with open('output', 'a', encoding='utf-8') as output_file:
    for i, contract_address in enumerate(tqdm_bar):
        current_serial_number = INDEX + i + 1
        COMMAND = (
            "slither --detect oracle-data-check,oracle-interface-check,oracle-protection-check " +
            f"{contract_address}" +
            " --etherscan-apikey YOUR_API_KEY"
        )
        try:
            result = subprocess.run(COMMAND, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True, check=True)
            output_file.write(f"--- 分析结果 {current_serial_number} / {len(contract_addresses)} - 合约地址：{contract_address} ---\n")
            output_file.write(result.stdout)
            output_file.write(result.stderr)
            output_file.write("\n" + "="*80 + "\n\n")
            output_file.flush()
        except subprocess.CalledProcessError as e:
            # 如果 Slither 命令执行失败，捕获错误并写入文件
            tqdm_bar.set_postfix({"错误": str(e)})
            output_file.write(f"--- 错误 {current_serial_number} / {len(contract_addresses)} - 分析 {contract_address} 时出错 ---\n")
            output_file.write(f"错误输出：{e.stderr}\n")
            output_file.write("\n" + "="*80 + "\n\n")
            output_file.flush()
        except Exception as e:
            # 捕获其他可能的异常
            tqdm_bar.set_postfix({"未知错误": str(e)})
            output_file.write(f"--- 未知错误 {current_serial_number} / {len(contract_addresses)} - 分析 {contract_address} 时发生未知错误 ---\n")
            output_file.write(f"错误信息：{e}\n")
            output_file.write("\n" + "="*80 + "\n\n")
            output_file.flush()