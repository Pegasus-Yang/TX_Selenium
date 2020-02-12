# Author:Pegasus-Yang
# Time:2020/2/10 16:24
from time import sleep

from PageObject0105.page.manage_tools_page import ManageToolsPage


class TestWxCompany:
    def setup(self):
        self.manage_tools_page = ManageToolsPage()

    def test_image_upload(self):
        """作业1：管理工具 -> 素材库 -> 图片 -> 上传"""
        upload_result = self.manage_tools_page.goto_material_page().upload_image('D:\\临时杂物\\5d7f51a0b0627.jpg')
        assert upload_result.start_page_image_num+1 == upload_result.end_page_image_num

    def teardown(self):
        pass
        # self.manage_tools_page.quit_driver()
