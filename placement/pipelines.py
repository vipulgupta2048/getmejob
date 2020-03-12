# -*- coding: utf-8 -*-


class OmitFieldPipeline(object):
    def process_item(self, item, spider):
        for key in item.copy():
            if not item[key]:
                item[key]=None
        return item
