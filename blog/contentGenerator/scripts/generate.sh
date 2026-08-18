SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd "$SCRIPT_DIR"

if [ ! -d ".venv" ]; then
    python3 -m venv .venv

    ./.venv/bin/pip3 install python-frontmatter
    ./.venv/bin/pip3 install markdown
fi 

./.venv/bin/python3 generateBlogPosts.py