from utils import *

class Dianping():
    def __init__(self):
        pass

    def dianping_get_hotel_price(self,keyword):
        try:
            # 通过搜索页，获取酒店页面
            # TODO：搜索页Driver加载过慢
            url_searchPage = 'https://www.dianping.com/search/keyword/2/0_' + keyword
            driver = webdriver.Chrome()
            driver.get(url_searchPage)
            # 名称检查
            name_hotel = driver.find_element_by_xpath("//div[@id='shop-all-list']/ul/li/div[2]/div/a/h4").text
            if name_hotel != keyword:
                print('原始名称为' + keyword + ',而正确名称为' + name_hotel + '。')
            url_hotel = driver.find_element_by_xpath("//div[@id='shop-all-list']/ul/li/div[2]/div/a").get_attribute(
                'href')

            # 登录酒店页面，获取酒店当晚指定房间类型的价格
            driver.get(url_hotel)
            price_hotel = driver.find_element_by_xpath(
                "//main[@id='poi-detail']/div[2]/div[2]/div[2]/div/div/div/div/div[2]/span/strong").text

            # 退出Driver
            driver.quit()

            return float(price_hotel)

        # 如果大众点评页面价格显示空缺，则将酒店价格标记为0元
        except Exception as e:
            print(e)
            price_hotel = 0
            return price_hotel