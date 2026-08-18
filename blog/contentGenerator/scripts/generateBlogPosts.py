import os
import shutil

from tagButtons import TagButton
from listPages import LIST_PAGE_OUTPUT_DIR, ListPage
from posts import DIR_POST_GENERATION_OUTPUT, DIR_POST_SOURCES, Post
from listPageEntries import ListPageEntry

# Do not execute this script manually. Use generate.sh to run it instead. This guarantees it
# runs in the right directory and uses the right virtual environment.

def main():
    # Remove old posts and tags directories
    if os.path.exists(DIR_POST_GENERATION_OUTPUT):
        shutil.rmtree(DIR_POST_GENERATION_OUTPUT)
    if os.path.exists(LIST_PAGE_OUTPUT_DIR):
        shutil.rmtree(LIST_PAGE_OUTPUT_DIR)

    # Load post content
    post_content_file_names = os.listdir(DIR_POST_SOURCES)
    post_content_file_names.sort(reverse=True)

    # Generate post objects and write them to the output dir
    posts: list[Post] = []
    for post_content_file_name in post_content_file_names:
        post = Post(post_content_file_name)
        posts.append(post)

    # Use the posts to generate list page entries
    list_page_entries: list[ListPageEntry] = []
    for post in posts: 
        list_page_entries.append(ListPageEntry(post))

    # Dict of tags pointing to lists of posts with that tag
    list_pages_to_create: dict[str, (TagButton, list[ListPageEntry])] = {}
    for list_page_entry in list_page_entries: 
        for tag_name in list_page_entry.tags: 
            if tag_name in list_pages_to_create: 
                list_pages_to_create[tag_name].append(list_page_entry)
            else:
                list_pages_to_create[tag_name] = [list_page_entry]

    # Generate all tag button objects 
    tag_buttons: list[TagButton] = []
    for tag_name in list_pages_to_create.keys():
        tag_buttons.append(TagButton(tag_name))

    # Add tag buttons to all posts and write to files
    for post in posts: 
        post.addTagButtons(tag_buttons)
        post.writeToFile()
    
    list_pages: list[ListPage] = []
    for tag_name, list_page_entries in list_pages_to_create.items(): 
        list_page = ListPage(tag_name, tag_buttons, list_page_entries)
        list_pages.append(list_page)
        list_page.writeToFile()

main()