import markdown
import frontmatter
import os

from common import FILE_NAME_INDEX
from tagButtons import TagButton
from templates import POST_TEMPLATE_DESCRIPTION, POST_TEMPLATE_FILE_NAME, Template

TAG_NAME_ALL = "All"
POST_PAGE_TAG_COLOUR = "orange"

FRONTMATTER_FIELD_TITLE = "title"
FRONTMATTER_FIELD_DESCRIPTION = "description"
FRONTMATTER_FIELD_DATE = "date"
FRONTMATTER_FIELD_TAGS = "tags"
FRONTMATTER_FIELD_CUSTOM_STYLE = "customStyle"
FRONTMATTER_FIELD_BACKGROUND_IMAGE_URL = "backgroundImage"
FRONTMATTER_FIELD_BACKGROUND_IMAGE_OFFSET = "backgroundImageOffset"

POST_TEMPLATE_STYLE_PLACEHOLDER = "/*style_placeholder*/"
POST_TITLE_PLACEHOLDER = "<!--title_placeholder-->"
POST_TEMPLATE_TAG_PLACEHOLDER = "<!--tag_button_placeholder-->"
POST_TEMPLATE_HTML_CONTENT_PLACEHOLDER = "<!--content_placeholder-->"

DIR_POST_SOURCES = "../sources"
DIR_POST_GENERATION_OUTPUT = "../../posts"

class Post:
    __slots__ = [
        'post_page_url_suffix', 
        'html_content', 
        'title', 
        'description', 
        'date', 
        'tags', 
        'background_image_url', 
        'background_image_offset'
    ]

    post_template = Template(POST_TEMPLATE_FILE_NAME, POST_TEMPLATE_DESCRIPTION)

    def __init__(self, post_content_file_name: str):
        # Load and parse the post source file
        post_source_file_relative_path = "/".join([DIR_POST_SOURCES, post_content_file_name])
        with open(post_source_file_relative_path, "r") as file:
            post_source_object = frontmatter.load(file)

        # Convert the post body from markdown to HTML
        body_html = markdown.markdown(post_source_object.content)

        # Extract the tags from the post and insert "All" as the first tag
        self.tags = post_source_object.get(FRONTMATTER_FIELD_TAGS)
        self.tags.insert(0, TAG_NAME_ALL)

        # Generate the URL suffix for this post by stripping .md extension from source file name
        self.post_page_url_suffix = post_content_file_name[:-3]

        # Retrieve other fields used for generating list page entries
        self.title = post_source_object.get(FRONTMATTER_FIELD_TITLE)
        self.description = post_source_object.get(FRONTMATTER_FIELD_DESCRIPTION)
        self.date = post_source_object.get(FRONTMATTER_FIELD_DATE)
        self.background_image_url = post_source_object.get(FRONTMATTER_FIELD_BACKGROUND_IMAGE_URL)
        self.background_image_offset = post_source_object.get(FRONTMATTER_FIELD_BACKGROUND_IMAGE_OFFSET)

        # Insert the body HTML into the post template to get the full HTML for the post page
        complete_html = self.post_template.content \
            .replace(POST_TITLE_PLACEHOLDER, self.title) \
            .replace(POST_TEMPLATE_HTML_CONTENT_PLACEHOLDER, body_html)

        # If there's a custom CSS rule specified in the frontmatter, insert it in the template's style placeholder
        post_custom_style_rule = post_source_object.get(FRONTMATTER_FIELD_CUSTOM_STYLE)
        if (post_custom_style_rule):
            complete_html = complete_html.replace(POST_TEMPLATE_STYLE_PLACEHOLDER, post_custom_style_rule)
        self.html_content = complete_html

    def addTagButtons(self, all_tag_buttons: list[TagButton]):
        tag_button_htmls: list[str] = []
        for tag_button in all_tag_buttons: 
            if tag_button.tag_name in self.tags:
                tag_button_html = tag_button.getWithColour(POST_PAGE_TAG_COLOUR)
                tag_button_htmls.append(tag_button_html)
        joined_tag_button_htmls = "\n".join(tag_button_htmls)
        self.html_content = self.html_content.replace(POST_TEMPLATE_TAG_PLACEHOLDER, joined_tag_button_htmls)

    def writeToFile(self):
        # Generate post output path
        post_output_relative_path = "/".join([DIR_POST_GENERATION_OUTPUT, self.post_page_url_suffix])
        post_file_relative_path = "/".join([post_output_relative_path, FILE_NAME_INDEX])

        # Write generated post content to its output directory
        os.makedirs(post_output_relative_path, exist_ok=True)
        with open(post_file_relative_path, "w") as file:
            file.write(self.html_content)