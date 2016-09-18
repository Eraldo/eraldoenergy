# from django.conf import settings
# from django.utils.html import format_html_join, format_html
# from wagtail.wagtailcore import hooks
#
# __author__ = 'eraldo'
#
#
# @hooks.register('insert_editor_js')
# def editor_js():
#     js_files = [
#         # 'global/js/hallo-code-snippet.js',
#         # 'global/js/hallo-code-block.js',
#         # 'global/js/hallo-tables.js',
#         # 'global/js/hallo-quote-snippet.js',
#         # 'global/js/hallo-htmledit.js',
#     ]
#
#     js_includes = format_html_join(
#         '\n',
#         '<script src="{0}{1}"></script>',
#         ((settings.STATIC_URL, filename) for filename in js_files)
#     )
#
#     return js_includes + format_html(
#         """
#         <script>
#             registerHalloPlugin('hallohtml');
#         </script>
#         """
#     )
