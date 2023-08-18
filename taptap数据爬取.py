import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# 设置Chrome驱动程序路径
chrome_driver_path = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"  # 替换为你的Chrome驱动程序路径

# 设置Chrome浏览器选项
chrome_options = Options()
chrome_options.add_argument("--auto-open-devtools-for-tabs")
# chrome_options.add_argument("--headless") # 无头模式，不显示浏览器窗口

# 启动Chrome浏览器
selenium_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

# 隐式等待
driver.implicitly_wait(10)  # 设置隐式等待时间，单位为秒

# 打开CSV文件并指定编码方式
with open('2023游戏号统计.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    rows = list(reader)

    # 创建新的CSV文件并打开以写入数据
    with open('output.csv', 'w', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.writer(outfile)

        for row in rows[1:]:
            name = row[1]
            search_link = 'https://www.taptap.com/search/' + name

            # 打开搜索链接
            driver.get(search_link)

            try:
                # 显式等待，等待搜索结果加载完成
                wait = WebDriverWait(driver, 5)  # 设置最长等待时间为5秒
                element = wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".ugc-moment-ui-card__content-title.list-heading-m14-w16")))
            except TimeoutException:
                print(f"超时，跳过 {name}")
                writer.writerow(row)  # 将当前行写入CSV文件
                continue

            # 点击第一个搜索结果
            first_result = driver.find_element(By.CSS_SELECTOR, ".text-hover")
            first_result_text = first_result.text  # 获取第一个搜索结果的文本
            if first_result_text != name:  # 如果文本与输入的name不匹配，开始下一次循环
                writer.writerow(row)  # 将当前行写入CSV文件
                continue

            ActionChains(driver).move_to_element(first_result).click().perform()

            try:
                # 等待新页面加载完成
                wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a.tap-router.tap-chip.tap-chip--leading.tap-chip--default.tap-chip--mobile")))
            except TimeoutException:
                print(f"新页面加载超时，跳过 {name}")
                writer.writerow(row)  # 将当前行写入CSV文件
                continue

            # 获取<a>标签元素
            elements = driver.find_elements(By.CSS_SELECTOR,
                                            "a.tap-router.tap-chip.tap-chip--leading.tap-chip--default.tap-chip--mobile")
            # 提取<a>标签内的文本内容
            if len(elements) > 0:
                tags = []  # 存储获取的标签
                for element in elements:
                    text_content = element.text
                    print(text_content)
                    tags.append(text_content)

                # 添加与获取的标签对应数量的空元素
                for _ in range(len(tags) - 1):
                    row.append('')

                # 将获取的标签添加到当前行的列表中
                row.extend(tags)
            else:
                print(f"无法获取 <a> 标签元素，跳过 {name}")

            writer.writerow(row)  # 将当前行写入CSV文件

# 关闭浏览器
driver.quit()
