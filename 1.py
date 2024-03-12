from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
# 从命令行参数获取日期和货币代码
date = sys.argv[1]
currency_code = sys.argv[2]

# 转换日期格式
formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"

# 转换货币代码为中文
currency_mapping = {
    "USD": "美元",
    "GBP": "英镑",
    "HKD": "港币",
    "CHF": "瑞士法郎",
    "DEM": "德国马克",
    "FRF": "法国法郎",
    "SGD": "新加坡元",
    "SEK": "瑞典克朗",
    "DKK": "丹麦克朗",
    "NOK": "挪威克朗",
    "CAD": "加拿大元",
    "AUD": "澳大利亚元",
    "EUR": "欧元",
    "MOP": "澳门元",
    "PHP": "菲律宾比索",
    "THB": "泰国铢",
    "NZD": "新西兰元",
    "KRW": "韩元",
    "RUB": "卢布",
    "MYR": "林吉特",
    "TWD": "新台币",
    "ESP": "西班牙比塞塔",
    "ITL": "意大利里拉",
    "NLG": "荷兰盾",
    "BEF": "比利时法郎",
    "FIM": "芬兰马克",
    "INR": "印度卢比",
    "IDR": "印尼卢比",
    "BRL": "巴西里亚尔",
    "AED": "阿联酋迪拉姆",
    "ZAR": "南非兰特",
    "SAR": "沙特里亚尔",
    "TRY": "土耳其里拉",
    # 货币代码的映射
}
currency_code_chinese = currency_mapping.get(currency_code, currency_code)

# 创建Chrome浏览器实例
driver = webdriver.Chrome()

try:
    # 打开中国银行外汇牌价网站
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    # 找到起始时间输入框，并写入日期
    start_date_input = driver.find_element_by_id("erectDate")
    start_date_input.clear()
    start_date_input.send_keys(formatted_date)

    # 找到结束时间输入框，并写入日期
    end_date_input = driver.find_element_by_id("nothing")
    end_date_input.clear()
    end_date_input.send_keys(formatted_date)

    # 找到牌价选择下拉列表
    select_element = driver.find_element_by_id("pjname")

    # 选择选项
    select = Select(select_element)
    select.select_by_visible_text(currency_code_chinese)

    # 点击查询按钮
    query_button = driver.find_element_by_css_selector("input.search_btn[onclick='executeSearch()']")
    query_button.click()

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "BOC_main")))

    # 找到表格
    table = driver.find_element_by_class_name("BOC_main")

    # 找到第一行数据
    rows = table.find_elements_by_tag_name("tr")
    first_row = rows[1]

    # 提取单元格的内容
    cells = first_row.find_elements_by_tag_name("td")
    selling_rate = cells[3].text.strip()

    # 打印第一行的价格
    print("现汇卖出价:", selling_rate)
    # 打开文件以写入数据
    with open('result.txt', 'w') as file:
        file.write(str(selling_rate))
except Exception as e:
    print("发生异常:", e)
finally:
    # 关闭浏览器
    driver.quit()
