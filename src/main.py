import json
import os
from urllib import request
from pathlib import Path
import shutil


from antidote import implements
from codemason import Codemason
from codemason.interfaces import (
    StartupHook,
    Reader,
    Generator,
    Writer,
    CodemasonInterface,
)
from codemason.interfaces.codemason import CodemasonDefaultInterface


from constants import PACKAGE_NAME
from pydantic_model_generator import load_type
from jinja import jinja_env




@implements(CodemasonInterface)
class SchemaOrg(CodemasonDefaultInterface):
    def __init__(self):
        settings = {}
        context = {
            "schemaorg": {"pydantic_class_models": {}}
        }
        super().__init__(settings=settings, context=context)


@implements(StartupHook)
class InitPackage(StartupHook):
    def run_startup_hook(self, codemason_interface: CodemasonInterface) -> None:
        if Path(PACKAGE_NAME).exists():
            shutil.rmtree(PACKAGE_NAME)
        os.makedirs(PACKAGE_NAME, exist_ok=True)


@implements(Reader)
class SchemaOrgRequest(Reader):
    def read(self, codemason_interface: CodemasonInterface) -> None:
        schema_org_request = request.urlopen(
            "https://schema.org/version/latest/schemaorg-current-https.jsonld"
        )
        schema_data = json.loads(schema_org_request.read().decode("utf-8"))
        schema_data = {node["@id"]: node for node in schema_data["@graph"]}
        codemason_interface.context["schemaorg"]["schema_data"] =  schema_data


@implements(Reader)
class CollectSchemaOrgTypes(Reader):
    depends_on = SchemaOrgRequest
    def read(self, codemason_interface: CodemasonInterface):
        codemason_interface.context["schemaorg"]["schemaorg_types"] = [
            k.strip().split(":")[-1]
            for k, v in codemason_interface.context["schemaorg"]["schema_data"].items()
            if v["@type"] != "rdf:Property"
        ]

@implements(Generator)
class PydanticModelGenerator(Generator):
    def generate(self, codemason_interface: CodemasonInterface):
         for type_ in codemason_interface.context["schemaorg"]["schemaorg_types"]:
             load_type(name=type_, context=codemason_interface.context)


@implements(Writer)
class PydanticModelWriter(Writer):
    def write(self, codemason_interface: CodemasonInterface):
        for model in codemason_interface.context["schemaorg"]["pydantic_class_models"].values():
            with open(
                f"{PACKAGE_NAME}/{model.valid_name}.py", "w"
            ) as model_file:
                with open(
                    Path(__file__).parent / "templates/model.py.tpl.j2"
                ) as template_file:
                    template = jinja_env.from_string(template_file.read())
                    template_args = dict(
                        schemaorg_version=os.getenv("SCHEMAORG_VERSION"),
                        model=model,
                    )
                template.stream(**template_args).dump(model_file)


@implements(Writer)
class InitWriter(Writer):
    def write(self, codemason_interface: CodemasonInterface) -> None:
        with open(
            f"{PACKAGE_NAME}/__init__.py", "w"
        ) as init_file:
            init_file.write('"""Generated Python Package Implementing https://schema.org/ types."""')

def main():
    cm = Codemason()
    cm.do_all()

if __name__ == "__main__":
    main()