# Author:Pegasus-Yang
# Time:2020/2/10 18:37
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObject0105.page.base_page import BasePage


class MaterialPage(BasePage):
    """企业微信管理工具-素材库页(frame#material)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#material'

    def _get_image_list_num(self, locat):
        """获取指定位置图片列表的长度"""
        page_image_list = (By.CSS_SELECTOR, '.material_picCard_text.js_pic_name_show')
        upload_image_list = (By.CSS_SELECTOR, '.ww_dialog_body .material_picCard_text.js_pic_name_show')
        if locat == 'page':
            self.clickable_wait(page_image_list)
            return len(self.find_elements(page_image_list))
        elif locat == 'upload':
            self.clickable_wait(upload_image_list)
            return len(self.find_elements(upload_image_list))

    def upload_image(self, image_path):
        """通过添加图片功能上传一张图片"""

        class UploadImageResult:
            """保存素材库图片上传中产生的数据"""
            start_page_image_num = 0
            start_upload_image_num = 0
            end_upload_image_num = 0
            end_page_image_num = 0

        result = UploadImageResult()
        image = (By.PARTIAL_LINK_TEXT, '图片')
        add_image = (By.PARTIAL_LINK_TEXT, '添加图片')
        upload_image = (By.CSS_SELECTOR, '#js_upload_input')
        ok_button = (By.PARTIAL_LINK_TEXT, '完成')
        self.clickable_wait(image)
        self.find_element(image).click()
        result.start_page_image_num = self._get_image_list_num('page')
        self.clickable_wait(add_image)
        self.find_element(add_image).click()
        self.find_element(upload_image).send_keys(image_path)
        WebDriverWait(self._driver, 10).until(
            lambda x: self._get_image_list_num('upload') ==1)
        result.end_upload_image_num = self._get_image_list_num('upload')
        self.find_element(ok_button).click()
        sleep(1)
        result.end_page_image_num = self._get_image_list_num('page')
        return result
