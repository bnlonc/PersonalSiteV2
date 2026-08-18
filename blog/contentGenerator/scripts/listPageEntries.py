from posts import Post

from templates import \
    LIST_PAGE_TEMPLATE_DESCRIPTION, \
    LIST_PAGE_TEMPLATE_FILE_NAME, \
    LIST_PAGE_ENTRY_TEMPLATE_FILE_NAME, \
    LIST_PAGE_ENTRY_TEMPLATE_DESCRIPTION, \
    Template

LIST_PAGE_TO_POST_LINK_PREFIX = "/blog/posts"

LIST_PAGE_ENTRY_URL_PLACEHOLDER = "$link_placeholder$"
LIST_PAGE_ENTRY_TITLE_PLACEHOLDER = "$title_placeholder$"
LIST_PAGE_ENTRY_DESCRIPTION_PLACEHOLDER = "$description_placeholder$"
LIST_PAGE_ENTRY_DATE_PLACEHOLDER = "$date_placeholder$"

LIST_PAGE_ENTRY_BACKGROUND_IMAGE_URL_PLACEHOLDER = "$background_image_url_placeholder$"
LIST_PAGE_ENTRY_BACKGROUND_IMAGE_RULE_TEMPLATE = \
    f"--background-image-url: url('{LIST_PAGE_ENTRY_BACKGROUND_IMAGE_URL_PLACEHOLDER}');"

LIST_PAGE_ENTRY_BACKGROUND_IMAGE_OFFSET_PLACEHOLDER = "$background_image_offset_placeholder$"
LIST_PAGE_ENTRY_BACKGROUND_OFFSET_RULE_TEMPLATE = \
    f"--background-offset: {LIST_PAGE_ENTRY_BACKGROUND_IMAGE_OFFSET_PLACEHOLDER};"

LIST_PAGE_ENTRY_BACKGROUND_IMAGE_RULE_PLACEHOLDER = "$background_image_rule_placeholder$"
LIST_PAGE_ENTRY_ADDITIONAL_CLASS_PLACEHOLDER = "$additional_class_placeholder$"
LIST_PAGE_ENTRY_BACKGROUND_CLASS_NAME = "backgroundImage"

class ListPageEntry: 
    __slots__ = ["html_content", "tags"]

    list_page_template = Template(LIST_PAGE_TEMPLATE_FILE_NAME, LIST_PAGE_TEMPLATE_DESCRIPTION)
    list_page_entry_template = Template(LIST_PAGE_ENTRY_TEMPLATE_FILE_NAME, LIST_PAGE_ENTRY_TEMPLATE_DESCRIPTION)

    def __init__(self, post: Post):
        list_page_to_post_relative_url = "/".join([LIST_PAGE_TO_POST_LINK_PREFIX, post.post_page_url_suffix])

        list_page_entry = self.list_page_entry_template.content \
            .replace(LIST_PAGE_ENTRY_URL_PLACEHOLDER, list_page_to_post_relative_url) \
            .replace(LIST_PAGE_ENTRY_TITLE_PLACEHOLDER, post.title) \
            .replace(LIST_PAGE_ENTRY_DESCRIPTION_PLACEHOLDER, post.description) \
            .replace(LIST_PAGE_ENTRY_DATE_PLACEHOLDER, post.date)

        if (post.background_image_url):
            rules = [
                LIST_PAGE_ENTRY_BACKGROUND_IMAGE_RULE_TEMPLATE \
                    .replace(LIST_PAGE_ENTRY_BACKGROUND_IMAGE_URL_PLACEHOLDER, post.background_image_url)
            ]
    
            if (post.background_image_offset):
                rules.append(LIST_PAGE_ENTRY_BACKGROUND_OFFSET_RULE_TEMPLATE \
                    .replace(LIST_PAGE_ENTRY_BACKGROUND_IMAGE_OFFSET_PLACEHOLDER, post.background_image_offset))
    
            list_page_entry = list_page_entry \
                .replace(LIST_PAGE_ENTRY_BACKGROUND_IMAGE_RULE_PLACEHOLDER, " ".join(rules)) \
                .replace(LIST_PAGE_ENTRY_ADDITIONAL_CLASS_PLACEHOLDER, LIST_PAGE_ENTRY_BACKGROUND_CLASS_NAME)
        else: 
            list_page_entry = list_page_entry \
                .replace(LIST_PAGE_ENTRY_BACKGROUND_IMAGE_RULE_PLACEHOLDER, "") \
                .replace(LIST_PAGE_ENTRY_ADDITIONAL_CLASS_PLACEHOLDER, "")
        
        self.html_content = list_page_entry

        self.tags = post.tags
