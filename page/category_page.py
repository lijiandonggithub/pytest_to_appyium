import random

import allure
import page

from base.base_action import BaseAction


class CategoryPage(BaseAction):




    # 随机点击 商品列表
    @allure.step(title='分类 点击 商品列表')
    def click_goods_list(self):
        goods_lists = self.find_elements(page.goods_list_button)
        goods_lists_count = len(goods_lists)
        goods_lists_index = random.randint(0, goods_lists_count - 1)
        goods_lists[goods_lists_index].click()