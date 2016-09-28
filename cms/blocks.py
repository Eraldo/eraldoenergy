from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailembeds.blocks import EmbedBlock as WagtailEmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HeadingBlock(blocks.CharBlock):
    class Meta:
        classname = 'full title'
        icon = 'title'
        template = 'widgets/heading.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['level'] = 1
        context['content'] = value
        return context


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        icon = 'pilcrow'
        template = 'widgets/richtext.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['content'] = value
        return context


class ImageBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        template = 'widgets/image.html'

    def get_context(self, value):
        context = super().get_context(value)
        context['url'] = value.get_rendition('max-1200x1200').url
        context['name'] = value.title
        return context


class EmbedBlock(WagtailEmbedBlock):
    class Meta:
        icon = 'media'
        template = 'widgets/embed.html'

    def get_context(self, value):
        context = super().get_context(value)
        embed = value
        context['embed'] = embed
        return context


BASE_BLOCKS = [
    ('heading', HeadingBlock()),
    ('rich_text', RichTextBlock()),
    ('image', ImageBlock()),
    ('embed', EmbedBlock()),
]

ALL_BLOCKS = BASE_BLOCKS + [
    ('html', RawHTMLBlock()),
]
