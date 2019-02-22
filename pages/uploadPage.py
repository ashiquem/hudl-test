class UploadPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.upload_input_class = "upload-file-input"
        self.upload_container_class = "upload-status"
        self.upload_header_class = "uni-headline--3"
        self.upload_selection_header_class = "upload-section--header"
        self.save_button_selector = "body > div.uni-modal__portal > div > div > div.uni-modal__footer > div > button"

    @property
    def select_files_button(self):
        return self.driver.find_element_by_class_name(self.upload_input_class)

    @property
    def upload_container(self):
        return self.driver.find_element_by_class_name(self.upload_container_class)

    @property
    def upload_header(self):
        return self.upload_container.find_element_by_class_name(self.upload_header_class)

    @property
    def upload_selection_header(self):
        return self.driver.find_element_by_class_name(self.upload_selection_header_class)

    @property
    def edit_share_button(self):
        return self.upload_selection_header.find_element_by_tag_name('button')

    @property
    def save_button(self):
        return self.driver.find_element_by_css_selector(self.save_button_selector)