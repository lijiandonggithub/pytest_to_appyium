
from base.base_action import BaseAction
import page
import allure


class AddressListPage(BaseAction):
    # 点击 新增地址
    @allure.step(title='地址列表 点击 添加地址')
    def click_add_address(self):
        self.find_element_with_scroll(page.add_address_button).click()

    # 获取 默认的姓名和电话的文字信息
    @allure.step(title='地址列表 获取 收件人和电话的标题')
    def get_default_receipt_name_text(self):
        return self.get_text(page.default_receipt_name_text_view)

    # 判断 默认标记 是否存在
    @allure.step(title='判断默认标记是否存在')
    def is_default_feature_exist(self):
        return self.is_feature_exist(page.is_default_feature)

    # 判断 删除按钮 是否存在
    @allure.step(title='判断删除按钮是否存在')
    def is_delete_exist(self):
        return self.is_feature_exist(page.delete_button)

    # 点击 默认地址
    @allure.step(title='地址列表 点击 默认地址')
    def click_default_address(self):
        self.click(page.is_default_feature)

    # 点击 编辑
    @allure.step(title='地址列表 点击 编辑')
    def click_edit(self):
        self.click(page.edit_button)

    # 点击 删除
    @allure.step(title='地址列表 点击 删除')
    def click_delete(self):
        self.click(page.delete_button)

    # 点击 确定
    def click_commit(self):
        self.click(page.commit_button)
