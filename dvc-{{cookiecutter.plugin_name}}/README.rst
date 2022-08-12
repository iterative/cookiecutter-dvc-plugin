{%- macro heading(text) -%}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(dvc-{{cookiecutter.plugin_name}}) }}

{{cookiecutter.plugin_name}} plugin for dvc
