DIR_TEMPLATES = "../templates"

LIST_PAGE_TEMPLATE_FILE_NAME = "listPageTemplate.shtml"
LIST_PAGE_TEMPLATE_DESCRIPTION = "List page template"

LIST_PAGE_ENTRY_TEMPLATE_FILE_NAME = "listPageEntryTemplate.shtml"
LIST_PAGE_ENTRY_TEMPLATE_DESCRIPTION = "List page post entry template"

POST_TEMPLATE_FILE_NAME = "blogPostTemplate.shtml"
POST_TEMPLATE_DESCRIPTION = "Blog post page template"

TAG_BUTTON_TEMPLATE_FILE_NAME = "tagButtonTemplate.shtml"
TAG_BUTTON_TEMPLATE_DESCRIPTION = "Tag button template"

class Template: 
    def __init__(self, file_name, description):
        self.file_name = file_name
        self.description = description

        template_file_name = "/".join([DIR_TEMPLATES, file_name])
        try:
            file = open(template_file_name, "r")
            template_contents = file.read()
            file.close()
            self.content = template_contents
        except FileNotFoundError: 
            error_message = (
                f"{description} file ({template_file_name}) not "
                f"found in templates folder at {DIR_TEMPLATES}!"
            )
            raise FileNotFoundError(error_message)
