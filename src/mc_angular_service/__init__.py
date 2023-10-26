from pathlib import Path
from importlib.resources import files

templates_dir = files("mc_angular_service") / "resources" / "template"

from model_codegen.models import DataModel, from_json
from model_codegen.utils.stringmanipulation import (
    to_camel_case,
    to_kebab_case,
    to_pascal_case
)


def generate(plugin_args):
    print(plugin_args)
    if len(plugin_args) != 2:
        raise ValueError("angular-service generate subcommand expects the following positional arguments `input`, `output_dir`.")
    input_path, output_path = plugin_args
    parent = Path(output_path)
    if parent.exists() and not parent.is_dir():
        raise ValueError(f"path '{parent}' is not a directory")
    

    input_model_path = Path(input_path)
    json_data = input_model_path.read_text()

    model: DataModel = from_json(json_data)

    for entity in model.entities:
        wd = create_directory(entity, parent)
        print(generate_service(entity, wd))

def create_directory(entity, parent: Path):
    folder: Path = parent / entity.name
    folder.mkdir(exist_ok=True, parents=True)
    return folder


def generate_service(entity, wd: Path):
    service_file_name = "service.ts"
    service_file = templates_dir / service_file_name
    service_text = replace_text_from_resource_file(entity, service_file)
    (wd /  f"{to_kebab_case(entity.name)}.service.ts").write_text(service_text)



def replace_text_from_resource_file(entity, ts_file):
    name = entity.name
    kebab_case = to_kebab_case(name)
    camel_case = to_camel_case(name)
    pascal_case = to_pascal_case(name)
    text = ts_file.read_text()
    return text \
        .replace("{kebab_case}", kebab_case) \
        .replace("{camel_case}", camel_case) \
        .replace("{pascal_case}", pascal_case)

 