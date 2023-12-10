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
    
    - Commercialisation d’un produit  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Commercialisation d’un produit.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/4_Commercialisation_Corr.pdf)
    - Élimination d’une substance dans le sang  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Élimination d’une substance dans le sang.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/7_Substance_Sang_Corr.pdf)
    - Étude de l’accidentologie  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de l’accidentologie.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/8_Accidentologie_Corr.pdf)
    - Étude de l’utilisation de supports musicaux  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de l’utilisation de supports musicaux.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/9_Supports_Musicaux_Corr.pdf)
    - Étude de population en Argentine et précarité  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude de population en Argentine et précarité.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/12_Population_Précarité_Argentine_Corr.pdf)
    - Etude d'une entreprise  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Etude d'une entreprise.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/3_Entreprise_Corr.pdf)
    - Étude d’une production  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Étude d’une production.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/6_Production_Corr.pdf)
    - Evolution de la population en Argentine  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Evolution de la population en Argentine.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/5_Population_Argentine_Corr.pdf)
    - Gestion d'un parc animalier  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Gestion d'un parc animalier.pdf)  -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/2_Parc_Animalier_Corr.pdf)
    - Organisation d'un marathon  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Organisation d'un marathon.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/1_Marathon_Corr.pdf)
    - Production de calculatrices  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Production de calculatrices.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/11_Calculatrices_Corr.pdf)
    - Tourisme  -  [:material-alpha-s-circle:{ .sujet }](/assets/sujets/TCmaths/Tourisme.pdf) -  [:material-alpha-c-circle:{ .corrige }](/assets/sujets/TCmaths/10_Tourisme_Corr.pdf)
