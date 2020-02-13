# Author:Pegasus-Yang
# Time:2020/2/10 18:37
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObject0105.page.base_page import BasePage


class MaterialPage(BasePage):
    """企业微信管理工具-素材库页(frame#material)"""
    _url = 'https://work.weixin.qq.com/wework_admin/frame#material'

    def _get_images_list_num(self, locat):
        """获取指定位置图片列表的长度"""
        if locat == 'page':
            image_list = (By.CSS_SELECTOR, '.material_picCard_text.js_pic_name_show')
        elif locat == 'upload':
            image_list = (By.CSS_SELECTOR, '.ww_dialog_body .material_picCard_text.js_pic_name_show')
        else:
            return False
        self._clickable_wait(image_list)
        return len(self._find_elements(image_list))

    def upload_image(self, image_path):
        """通过添加图片功能上传一张图片"""

        class UploadImageResult:
            """保存素材库图片上传中产生的数据"""
            start_page_images_num = 0
            start_upload_images_num = 0
            end_upload_images_num = 0
            end_page_images_num = 0

        result = UploadImageResult()
        image = (By.PARTIAL_LINK_TEXT, '图片')
        add_image = (By.PARTIAL_LINK_TEXT, '添加图片')
        upload_image = (By.CSS_SELECTOR, '#js_upload_input')
        ok_button = (By.PARTIAL_LINK_TEXT, '完成')
        self._click_element(image)
        result.start_page_images_num = self._get_images_list_num('page')
        self._click_element(add_image)
        self._find_element(upload_image).send_keys(image_path)
        WebDriverWait(self._driver, 10).until(
            lambda x: self._get_images_list_num('upload') == 1)
        result.end_upload_images_num = self._get_images_list_num('upload')
        self._find_element(ok_button).click()
        sleep(1)
        result.end_page_images_num = self._get_images_list_num('page')
        return result
