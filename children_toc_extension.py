from markdown.extensions.toc import TocExtension
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

class ChildTocTreeprocessor(Treeprocessor):
    def __init__(self, page):
        self.page = page
        super().__init__()

    def run(self, root):
        # Get the current page
        page = self.page
        if not page or not page.children:
            return

        # Create a new TOC extension
        toc_extension = TocExtension()

        # Generate a TOC for each child page and insert it into the parse tree
        for child_page in page.children:
            child_toc = toc_extension.build_toc_tree(child_page.content)
            if child_toc:
                toc_heading = self.md.htmlStash.store('<h2>{}</h2>'.format(child_page.title))
                child_toc.insert(0, toc_heading)
                root.append(child_toc)

class ChildTocExtension(Extension):
    def __init__(self, page=None, title='Child Pages', **kwargs):
        self.config = {
            'title': [title, 'Title to display above child page TOCs']
        }
        self.page = page
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.treeprocessors.register(ChildTocTreeprocessor(self.page), 'childtoc', 25)

        # Add the title to the global TOC
        title = self.getConfig('title')[0]
        toc = md.toc
        toc = toc.replace('</nav>', '</nav><h2>{}</h2>'.format(title))
        md.toc = toc

