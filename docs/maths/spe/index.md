# Tronc Commun Maths 1ère

!!! info "Concerne Kélian, Valentin et Lilou-Ann"

{% set parent_page = page.parent %}
{% set child_pages = parent_page.children if parent_page else [] %}
{% if child_pages %}
<div class="toc">
  <h2>Au programme</h2>
  <ul>
  {% for child_page in child_pages %}
    {% if child_page != page %}
    <li><a href="/{{ child_page.url }}">Chapitre {{ loop.index - 1 }}: {{ child_page.title }}</a></li>
{% endif %}
  {% endfor %}
  </ul>
</div>
{% endif %}
