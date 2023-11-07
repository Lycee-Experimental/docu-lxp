# Tronc Commun Maths 1ère

!!! info "Concerne tou.te.s les premières SAUF Kélian, Valentin et Lilou-Ann"

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

??? question "Sujets BAC"
    :material-alpha-s-circle:{ .sujet} : Sujets  
    :material-alpha-c-circle:{ .corrige } : Corrigés  
    :material-alpha-i-circle:{ .indice } : Indices
    
    - Commercialisation d’un produit  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Commercialisation d’un produit.pdf)
    - Élimination d’une substance dans le sang  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Élimination d’une substance dans le sang.pdf)
    - Étude de l’accidentologie  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de l’accidentologie.pdf)
    - Étude de l’utilisation de supports musicaux  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de l’utilisation de supports musicaux.pdf)
    - Étude de population en Argentine et précarité  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de population en Argentine et précarité.pdf)
    - Etude d'une entreprise  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Etude d'une entreprise.pdf)
    - Étude d’une production  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude d’une production.pdf)
    - Evolution de la population en Argentine  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Evolution de la population en Argentine.pdf)
    - Gestion d'un parc animalier  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Gestion d'un parc animalier.pdf)
    - Organisation d'un marathon  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Organisation d'un marathon.pdf)
    - Production de calculatrices  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Production de calculatrices.pdf)
    - Tourisme  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Tourisme.pdf)