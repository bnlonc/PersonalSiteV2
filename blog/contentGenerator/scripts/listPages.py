import os

from common import FILE_NAME_INDEX
from listPageEntries import ListPageEntry
from tagButtons import TAG_BUTTON_CONTENT_PLACEHOLDER, TagButton
from templates import Template, LIST_PAGE_TEMPLATE_FILE_NAME, LIST_PAGE_TEMPLATE_DESCRIPTION

LIST_PAGE_OUTPUT_DIR = "../../tags"

TAG_BUTTONS_ACTIVE_COLOUR = "orange"
TAG_BUTTONS_INACTIVE_COLOUR = "grey"

BODY_CONTENT_PLACEHOLDER = "<!--body_content_placeholder-->"

class ListPage:
    __slots__ = ["tag_name", "html_content"]

    list_page_template = Template(LIST_PAGE_TEMPLATE_FILE_NAME, LIST_PAGE_TEMPLATE_DESCRIPTION)

    def __init__(self, tag_name: str, all_tag_buttons: list[TagButton], all_list_page_entries: list[ListPageEntry]):
        self.tag_name = tag_name

        all_entry_content = "\n".join(list(map(lambda entry: entry.html_content, all_list_page_entries)))

        tag_button_htmls: list[str] = []
        for tag_button in all_tag_buttons:
            if (tag_button.tag_name == tag_name):
                tag_button_htmls.append(tag_button.getWithColour(TAG_BUTTONS_ACTIVE_COLOUR))
            else:
                tag_button_htmls.append(tag_button.getWithColour(TAG_BUTTONS_INACTIVE_COLOUR))
        tag_button_joined_htmls = "\n".join(tag_button_htmls)

        self.html_content = self.list_page_template.content \
            .replace(TAG_BUTTON_CONTENT_PLACEHOLDER, tag_button_joined_htmls) \
            .replace(BODY_CONTENT_PLACEHOLDER, all_entry_content)

    def writeToFile(self):
        list_page_file_name: str
        page_output_path = "/".join([LIST_PAGE_OUTPUT_DIR, self.tag_name.lower()])
        os.makedirs(page_output_path, exist_ok=True)

        list_page_file_name = "/".join([page_output_path, FILE_NAME_INDEX])
        with open(list_page_file_name, "w") as file:
            file.write(self.html_content)
        