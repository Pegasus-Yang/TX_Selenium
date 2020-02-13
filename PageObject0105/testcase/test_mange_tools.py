# Author:Pegasus-Yang
# Time:2020/2/10 16:24
import pytest

from PageObject0105.page.manage_tools_page import ManageToolsPage
from PageObject0105.tools.common_tools import get_abs_path

image_path = ['../data/天马.jpg']


class TestWxCompany:
    def setup(self):
        self.manage_tools_page = ManageToolsPage()

    @pytest.mark.parametrize('upload_image_path', image_path)
    def test_image_upload(self, upload_image_path):
        print(upload_image_path)
        """作业1：管理工具 -> 素材库 -> 图片 -> 上传"""
        upload_result = self.manage_tools_page.goto_material_page().upload_image(get_abs_path(upload_image_path))
        assert upload_result.start_page_images_num + 1 == upload_result.end_page_images_num

    def teardown(self):
        pass
        self.manage_tools_page.quit_driver()
