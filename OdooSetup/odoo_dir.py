import os

def odoo_dir(package_name, base_path):
    # Define the base directory for the Odoo module
    base_dir = os.path.join(base_path, package_name)
    
    # Define the subdirectories to create
    subdirectories = [
        os.path.join(base_dir, 'models'),
        os.path.join(base_dir, 'views'),
        os.path.join(base_dir, 'data'),
        os.path.join(base_dir, 'security'),
        os.path.join(base_dir, 'controllers'),
        os.path.join(base_dir, 'reports'),  # Adding reports directory
    ]
    
    # Define the files and their content with the correct paths using f-strings
    files = {
        os.path.join(base_dir, '__init__.py'): """# Inicializa el módulo Odoo
""",
        os.path.join(base_dir, '__manifest__.py'): f"""# -*- coding: utf-8 -*-
{{
    'name': '{package_name}',
    'version': '1.0',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'security/{package_name}_security.xml',
        'views/views.xml',
        'reports/{package_name}_report.xml'
    ],
    'installable': True,
    'application': True,
    'description': 'Descripción del módulo {package_name}.',
    'author': 'Tu Nombre',
    'license': 'LGPL-3',
}}
""",
        os.path.join(base_dir, 'README.md'): f"""# {package_name}

Este módulo Odoo permite [breve descripción de la funcionalidad].
""",
        os.path.join(base_dir, 'requirements.txt'): """# Lista de dependencias del módulo

# Ejemplo de dependencia
# odoo
""",
        # Adding __init__.py in models and controllers directories
        os.path.join(base_dir, 'models', '__init__.py'): """# Inicializa los modelos de Odoo
""",
        os.path.join(base_dir, 'controllers', '__init__.py'): """# Inicializa los controladores de Odoo
""",
        # Adding views.xml in views directory
        os.path.join(base_dir, 'views', 'views.xml'): f"""<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record id="view_form_{package_name}" model="ir.ui.view">
        <field name="name">view.form.{package_name}</field>
        <field name="model">{package_name}.model</field>
        <field name="arch" type="xml">
            <form string="{package_name}">
                <sheet>
                    <group>
                        <field name="name"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
</odoo>
""",
        # Adding data.xml in data directory
        os.path.join(base_dir, 'data', 'data.xml'): f"""<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <!-- Data for {package_name} -->
</odoo>
""",
        # Adding ir.model.access.csv in security directory
        os.path.join(base_dir, 'security', 'ir.model.access.csv'): f"""id,name,model_id:id,group_id,perm_read,perm_write,perm_create,perm_unlink
access_{package_name}_model,access_{package_name}_model,model_{package_name}_model,,1,1,1,1
""",
        # Adding custom security file in security directory
        os.path.join(base_dir, 'security', f'{package_name}_security.xml'): f"""<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <!-- Security groups for {package_name} -->
    </data>
</odoo>
""",
        # Adding base report XML in reports directory
        os.path.join(base_dir, 'reports', f'{package_name}_report.xml'): f"""<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <template id="{package_name}_report_template">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="doc">
                <div class="page">
                    <!-- Report Content for {package_name} -->
                </div>
            </t>
        </t>
    </template>

    <report 
        id="{package_name}_report"
        model="{package_name}.model"
        string="Sample Report"
        report_type="qweb-pdf"
        name="{package_name}_report_template"
        file="{package_name}_report_template"
        attachment_use="False"
    />
</odoo>
"""
    }
    
    # Create the base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create subdirectories
    for subdirectory in subdirectories:
        os.makedirs(subdirectory, exist_ok=True)

    # Create files with example content
    for file_path, content in files.items():
        # Verifica si el archivo ya existe
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)  # f-strings already use the package_name
        else:
            print(f"El archivo '{file_path}' ya existe y no se creará de nuevo.")

# Solicita el nombre del módulo y la ruta base al usuario
package_name = input("Introduce el nombre de tu módulo Odoo: ")
base_path = input("Introduce la ruta donde deseas crear el directorio: ")

# Crea la estructura del módulo Odoo
odoo_dir(package_name, base_path)
