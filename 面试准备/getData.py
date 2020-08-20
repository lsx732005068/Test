# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import xlwt


driver = webdriver.Ie()
driver.implicitly_wait(15)
driver.get("http://221.226.86.137/nanjingjianshe/JSGCZtbMis/login.aspx");
driver.maximize_window()
driver.find_element_by_id("txtUserName").send_keys("")
driver.find_element_by_id("txtPwd").send_keys("future123")
driver.find_element_by_id("Imagebutton1").click()
driver.get("http://221.226.86.137/nanjingjianshe/ZHManageMis/Pages/Jsgc_ChaXun/TouBiaoFile.aspx");
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSearch").click()
time.sleep(3)
driver.find_element_by_id("ctl00_ContentPlaceHolder1_DanWeiName").send_keys("中皓")
driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnOK").click()
time.sleep(15)

# 创建工作簿
wbk = xlwt.Workbook(encoding='utf=8', style_compression=0)
# 创建工作表
sheet = wbk.add_sheet('tbData', cell_overwrite_ok=True)

count = 0
while count < 2:
    table_tr_list = driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_Datagrid1\"]/tbody").\
        find_elements_by_tag_name("tr")
    for r, tr in enumerate(table_tr_list):
        table_td_list = tr.find_elements_by_tag_name('td')
        for c, td in enumerate(table_td_list):
            sheet.write(r+(count*21), c, td.text)
    if count == 0:
        nextPage = driver.find_element_by_id("ctl00_ContentPlaceHolder1_Pager").\
            find_element_by_css_selector("img[src=\"http://221.226.86.137/nanjingjianshe/images/page/nextn.gif\"]")
        nextPage.click()
    count += 1
    time.sleep(8)

# 保存该文件，文件必须存在
wbk.save(r'E:\testExcel\toubiaoData.xls')
driver.quit()

# if __name__ == '__main__':
#     getData()
