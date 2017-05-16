from lxml import html


class Scraper:
    def __init__(self, dom):
        self.dom = dom

    @staticmethod
    def html_dom(html_string):
        return html.fromstring(html_string)

    @staticmethod
    def get_text(element):
        return element.xpath('text()')

    @staticmethod
    def get_attribute(name, element):
        return element.xpath('attribute::'+name)[0]

    def get_element_by_id(self, tag_id, root=None):
        if root is None:
            return self.dom.xpath('//*[@id="'+tag_id+'"]')[0]
        else:
            return root.xpath('//*[@id="'+tag_id+'"]')[0]

    def get_element_by_attr(self, attr_name, attr_value, root=None):
        if root is None:
            return self.dom.xpath('//*[@' + attr_name + '="' + attr_value + '"]')
        else:
            return root.xpath('//*[@' + attr_name + '="' + attr_value + '"]')

    def get_elements_by_class_name(self, name, root=None):
        if root is None:
            return self.dom.xpath('//*[@class="' + name + '"]')
        else:
            return root.xpath('//*[@class="' + name + '"]')

    def get_elements_by_tag_name(self, name, root=None):
        if root is None:
            return self.dom.xpath('//' + name)
        else:
            return root.xpath('//' + name)

    def get_custom_filter(self, custom_filter, root=None):
        if root is None:
            return self.dom.xpath(custom_filter)
        else:
            return root.xpath(custom_filter)
