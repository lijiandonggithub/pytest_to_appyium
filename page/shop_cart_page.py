import page
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class ShopCartPage(BaseAction):


    # 点击 全选
    @allure.step(title='购物车 点击 全选')
    def click_select_all(self):
        self.click(page.select_all_button)

    # 编辑 按钮
    edit_button = By.XPATH, "//*[@text='编辑']"

    # 点击 编辑
    @allure.step(title='购物车 点击 编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 完成 按钮
    commit_button = By.XPATH, "//*[@text='完成']"

    # 点击 完成
    @allure.step(title='购物车 点击 完成')
    def click_commit(self):
        self.click(self.commit_button)

    # 加号 按钮
    add_button = By.ID, "com.yunmall.lc:id/iv_add"

    # 点击 加号
    @allure.step(title='购物车 点击 加号')
    def click_add(self):
        self.click(self.add_button)

    def get_price(self):
        # 获取单价的文字
        price_text = self.get_text(page.price_feature)
        # 通过 deal_with_price 去掉前面的人民币符号，并且转化成哼float类型
        return self.deal_with_price(price_text)

    def get_all_price(self):
        # 获取单价的文字
        price_text = self.get_text(page.all_price_feature)
        # 通过 deal_with_price 去掉前面的人民币符号，并且转化成哼float类型
        return self.deal_with_price(price_text)

    def deal_with_price(self, price):
        "￥ 25.80"
        return float(price[2:])


    # 点击 删除
    def click_delete(self):
        self.click(page.delete_button)

    # 点击 确认
    def click_yes(self):
        self.click(page.yes_button)

    # 判断购物车是否为空
    def is_shop_cart_empty(self):
        xpath = By.XPATH, "//*[contains(@text,'购物车还是空的')]"
        return self.is_feature_exist(xpath)

