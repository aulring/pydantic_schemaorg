import datetime
import json
import os
import shutil
from dataclasses import dataclass
from http.client import HTTPResponse
from pathlib import Path
from urllib import request

from constants import data_type_map, PACKAGE_NAME, data_type_specificity
from jinja import jinja_env
from schema_org import SchemaOrg

THIS_PATH = Path(__file__).parent


@dataclass
class Models:
    attr_models: list
    models: list


def write_base_class():
    with open(f"{PACKAGE_NAME}/SchemaOrgBase.py", "w") as model_file:
        with open(
                THIS_PATH / "templates/schema_org_base.py.tpl"
        ) as template_file:
            template = jinja_env.from_string(template_file.read())
            template_args = dict(
                schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                commit=os.getenv("COMMIT"),
                timestamp=datetime.datetime.now(),
            )
        template.stream(**template_args).dump(model_file)


def copy_utils():
    os.makedirs(f'{PACKAGE_NAME}/ISO8601', exist_ok=True)
    for file in os.listdir(f'{THIS_PATH}/ISO8601'):
        if file.endswith('.py'):
            shutil.copy(f'{THIS_PATH}/ISO8601/{file}', f'{PACKAGE_NAME}/ISO8601')


def init_package():
    shutil.rmtree(PACKAGE_NAME)
    os.makedirs(PACKAGE_NAME, exist_ok=True)
    copy_utils()


if __name__ == "__main__":
    init_package()
    write_base_class()
    schema_org_request: HTTPResponse = request.urlopen(
        "https://schema.org/version/latest/schemaorg-current-https.jsonld"
    )
    schema_data = json.loads(schema_org_request.read().decode("utf-8"))
    schema_data = {node["@id"]: node for node in schema_data["@graph"]}
    schema_org_api = SchemaOrg(schema_data, data_type_map, data_type_specificity)
    tpls_dict={"tpls":[], "tpl_attrs": []}
    for class_ in schema_org_api.get_all_classes():
        schema_org_api.load_type(class_, tpls=tpls_dict)
    # with open("schema_models.py", "w") as f:
    #     for tpl in tpls_dict["tpls"]:
    #         f.write(tpl)
    #         f.write("\n\n")

    with open(f"{PACKAGE_NAME}/schema_model.py", "w") as model_file:
        with open(
                Path(__file__).parent / "templates/schema_model.py.tpl"
        ) as template_file:
            template = jinja_env.from_string(template_file.read())
        #template.stream(**template_args).dump(model_file)
        tpls_dict["tpl_attrs"]
        models = Models(attr_models=tpls_dict["tpl_attrs"], models=tpls_dict["tpls"])
        rendered = template.render(models=models)
        model_file.write(rendered)
    schema_org_api.write_init()
