# {{ title }}

**Autor: {{ author }}**

{% for chapter in chapters %}
## {{ chapter.title }}

{{ chapter.content }}

{% if chapter.images %}
{% for img in chapter.images %}
![Imagem]({{ img }})
{% endfor %}
{% endif %}

{% endfor %}
