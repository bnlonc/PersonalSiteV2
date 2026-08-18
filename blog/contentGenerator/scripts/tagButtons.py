from templates import TAG_BUTTON_TEMPLATE_DESCRIPTION, TAG_BUTTON_TEMPLATE_FILE_NAME, Template

TAG_BUTTON_CONTENT_PLACEHOLDER = "<!--tag_button_placeholder-->"

TAG_BUTTONS_TAG_PAGE_NAME_PLACEHOLDER = "$tagPageName$"
TAG_BUTTONS_TAG_NAME_PLACEHOLDER = "$tagName$"
TAG_BUTTONS_COLOUR_PLACEHOLDER = "$colour$"

class TagButton: 
    __slots__ = ["tag_name", "html_content"]

    tag_button_template = Template(TAG_BUTTON_TEMPLATE_FILE_NAME, TAG_BUTTON_TEMPLATE_DESCRIPTION)

    def __init__(self, tag_name):
        self.html_content = self.tag_button_template.content \
            .replace(TAG_BUTTONS_TAG_NAME_PLACEHOLDER, tag_name) \
            .replace(TAG_BUTTONS_TAG_PAGE_NAME_PLACEHOLDER, tag_name.lower())
        self.tag_name = tag_name

    def getWithColour(self, colour):
        return self.html_content.replace(TAG_BUTTONS_COLOUR_PLACEHOLDER, colour) 
