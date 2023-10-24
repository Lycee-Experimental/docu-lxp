def custom_formatter(source, language, css_class, options, md, classes=None, id_value='', attrs=None, **kwargs):
    return '```'+css_class+'\n'+source+'\n```'