class {{ model.valid_name }}({{model.parents| sort(attribute='depth', reverse=True) | map(attribute='valid_name') | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See: https://schema.org/{{ model.name }}
    Model depth: {{model.depth}}
    """
    type_: str = Field(default="{{ model.name }}", alias='@type', const=True)
    {% for field in model.fields -%}
    {{ field.valid_name }}: {{ field.type }} = Field(
        default=None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | replace('\\n','\n') | format_description }}",
    )
    {% endfor %}