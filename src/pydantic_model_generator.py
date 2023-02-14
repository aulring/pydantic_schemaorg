from typing import Dict, List, Set, Tuple

from models import ModelAttributes, AttributeType
from constants import DATA_TYPE_MAP, DATA_TYPE_SPECIFICITY


def to_set(_object, prop="@id") -> Set[str]:
    if isinstance(_object, list):
        return set(item[prop] if prop is not None else item for item in _object)
    elif _object is None:
        return set()
    else:
        return {_object[prop] if prop is not None else _object}


def fields_for_model(name: str, context: dict) -> List[Tuple[str, Dict]]:
    return [
        (key.strip().split(":")[-1], field)
        for key, field in context["schemaorg"]["schema_data"].items()
        if (
            field.get("@type") == "rdf:Property"
            and f"schema:{name}" in to_set(field.get("schema:domainIncludes"))
        )
    ]

def get_including_types(field: dict) -> List[str]:
    return [
        incl_type.strip().split(":")[-1]
        for incl_type in to_set(field.get("schema:rangeIncludes"))
    ]


def cast_description(description):
    return description.replace("\n", "") if isinstance(description, str) else description["@value"]

def extract_fields(name: str, context: dict) -> List[AttributeType]:
    fields  = []
    for key, field in fields_for_model(name=name, context=context):
        field_parent_types = get_including_types(field)
        field_types = [type_name for type_name in field_parent_types]
        pydantic_types = ()
        for field_type in sorted(
            field_types,
            key=lambda ft: DATA_TYPE_SPECIFICITY.get(ft, 0),
            reverse=True,
        ):
            if field_type in DATA_TYPE_MAP:
                pydantic_types += (DATA_TYPE_MAP[field_type][0],)
            if name != field_type:
                pydantic_types += (f"" f"Any",)
            else: 
                #use any as hack for self ref
                pydantic_types += (f"Any",)

        if field_parent_types != field_types:
            pydantic_types = pydantic_types + ("Any",)
        if not "str" in pydantic_types:
            pydantic_types += ("str",)
        type_tuple = ", ".join(list(set(pydantic_types)))
        if not pydantic_types:
            continue
        elif len(pydantic_types) > 1:
            optional = pydantic_types[-1] != "Any"
            pydantic_types = f"Union[List[Union[{type_tuple}]], {type_tuple}]"
            if optional:
                pydantic_types = f"Optional[{pydantic_types}]"
        else:
            pydantic_types = (
                type_tuple
                if type_tuple == "Any"
                else f"Optional[Union[List[{type_tuple}], {type_tuple}]]"
            )
            #TODO: unpack fields to doc string... cuz we need to create dynamically, but it's still nice to have the description
        fields.append(
            AttributeType(
                name=key,
                description=cast_description(
                    context["schemaorg"]["schema_data"][f"schema:{key}"].get("rdfs:comment", "")
                ),
                type=pydantic_types,
            )
        )
    return fields


def extract_parents(node, context) -> Tuple[List[ModelAttributes], list, int]:
    parent_names = set(
        reference.strip().split(":")[-1]
        for reference in to_set(node.get("rdfs:subClassOf", []))
    )
    node_types = node["@type"] if type(node["@type"]) == list else [node["@type"]]
    for node_type in node_types:
        if node_type.startswith("schema:"):
            parent_names.add(node_type.strip().split(":")[-1])
    parents: List[ModelAttributes] = []
    for parent_name in parent_names:
        parents.append(load_type(parent_name, context=context))
    parent_depth = next(
        map(lambda y: y.depth, sorted(parents, key=lambda x: x.depth)), 0
    )
    sorted_parents = list(
        map(
            lambda y: y,
            sorted(parents, key=lambda x: x.depth, reverse=True),
        )
    )
    depth = parent_depth + 1
    if not sorted_parents:
        sorted_parents = [
            ModelAttributes(
                name="SchemaOrgBase",
                description="",
                fields=[],
                parents=[]
            )
        ]
    return sorted_parents, depth


def load_type(name: str, context: dict) -> ModelAttributes:
    if name in context["schemaorg"]["pydantic_class_models"]:
        print(f"{name} exists, skipping..")
        return context["schemaorg"]["pydantic_class_models"][name]
    try:
        node = context["schemaorg"]["schema_data"][f"schema:{name}"]
    except KeyError:
        raise ValueError(f"Model {name} does not exist")
    
    fields = extract_fields(name=name, context=context)


    parents, depth = extract_parents(node, context)
    parent_fields = []
    for parent in parents:
        parent_fields += parent.fields

    context["schemaorg"]["pydantic_class_models"][name] = ModelAttributes(
        name=name,
        description=cast_description(node.get("rdfs:comment", "")),
        fields=[*parent_fields, *fields],
        parents=parents,
        depth=depth,
    )
    return context["schemaorg"]["pydantic_class_models"][name]

