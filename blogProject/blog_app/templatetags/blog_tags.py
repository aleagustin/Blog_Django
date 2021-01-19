from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown



#Importante en el HTML donde quiero usar estos metodos debo {% load blog_tags%}

register = template.Library()

#Contador de posts
@register.simple_tag
def total_posts():
    return Post.published.count()


##Barra lateral con listado de post
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}    



@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
                                total_comments=Count('comments')
                                ).order_by('-total_comments')[:count]



@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


