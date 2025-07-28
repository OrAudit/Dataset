"""
Extracting and processing contract data from an HTML file of contract searching from Etherscan.
"""
import os
import re
import pandas as pd
from bs4 import BeautifulSoup

# Define the directory containing the HTML files and output CSV
HTML_DIR = 'chronicle/IChronicle'  # 设定存放HTML文件的目录
OUTPUT = 'chronicle/IChronicle/contracts.csv'

# 获取指定目录下的所有HTML文件
html_files = [f for f in os.listdir(HTML_DIR) if f.endswith('.html')]

# 处理每个HTML文件
data = []
for html_file in html_files:
    try:
        with open(os.path.join(HTML_DIR, html_file), 'r', encoding='utf-8') as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        cards = soup.find_all('div', class_='card')

        for card in cards:
            try:
                # Contract Address (假设它在第一个 <a> 标签内)
                contract_address = card.find('a', href=True).text.strip()
                # Contract Name (在 <i class="far fa-file-user"> 后面)
                name_div = card.find('i', class_='far fa-file-user text-muted')
                contract_name = name_div.find_next(string=True).strip() if name_div else 'N/A'
                # Publish Date (在 <i class="far fa-calendar-day"> 后面)
                date_div = card.find('i', class_='far fa-calendar-day text-muted')
                publish_date = date_div.find_next(string=True).strip() if date_div else 'N/A'
                # Transactions (在 <i class="far fa-exchange-alt"> 后面)
                tx_div = card.find('i', class_='far fa-exchange-alt text-muted')
                transactions = tx_div.find_next('a').text.strip() if tx_div else 'N/A'
                transactions_number = re.sub(r'\D', '', transactions)  # 删除非数字字符

                # 追加到数据列表
                data.append({
                    'Address': contract_address,
                    'Name': contract_name,
                    'Date': publish_date,
                    'Transactions': transactions_number  # 只保留数字部分
                })
            except AttributeError as e:
                print(f'Error: Attribute missing or wrong attribute format in {html_file} - {e}')
            except ValueError as e:
                print(f'Error: Value issue in {html_file} - {e}')

    except FileNotFoundError:
        print(f"Error: File not found - {html_file}")
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

# 如果文件存在，则以追加模式打开，不写入列名；否则新建文件并写入列名
if os.path.exists(OUTPUT):
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT, mode='a', header=False, index=False, encoding='utf-8-sig')  # 追加数据
else:
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT, mode='w', header=True, index=False, encoding='utf-8-sig')  # 创建新文件并写入列名

print("success")
