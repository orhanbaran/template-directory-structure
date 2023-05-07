import os

PROJECT_CREATED_FLAG = False

def create_project():
    global PROJECT_CREATED_FLAG

    if PROJECT_CREATED_FLAG:
        print("Project already created.")
        return
    project_name = input("Enter the project name: ")
    project_dir = os.path.join(os.getcwd(), project_name)

    # Create project directory
    os.makedirs(project_dir, exist_ok=True)

    # Create subdirectories
    src_dir = os.path.join(project_dir, 'src')
    os.makedirs(src_dir, exist_ok=True)

    module1_dir = os.path.join(src_dir, 'module1')
    os.makedirs(module1_dir, exist_ok=True)

    module2_dir = os.path.join(src_dir, 'module2')
    os.makedirs(module2_dir, exist_ok=True)

    utils_dir = os.path.join(src_dir, 'utils')
    os.makedirs(utils_dir, exist_ok=True)

    data_dir = os.path.join(project_dir, 'data')
    os.makedirs(os.path.join(data_dir, 'raw'), exist_ok=True)
    os.makedirs(os.path.join(data_dir, 'processed'), exist_ok=True)

    notebooks_dir = os.path.join(project_dir, 'notebooks')
    os.makedirs(notebooks_dir, exist_ok=True)

    tests_dir = os.path.join(project_dir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)

    # Create source files
    with open(os.path.join(src_dir, '__init__.py'), 'w') as f:
        pass

    with open(os.path.join(module1_dir, '__init__.py'), 'w') as f:
        pass

    with open(os.path.join(module1_dir, 'module1.py'), 'w') as f:
        f.write('# Module 1')

    with open(os.path.join(module2_dir, '__init__.py'), 'w') as f:
        pass

    with open(os.path.join(module2_dir, 'module2.py'), 'w') as f:
        f.write('# Module 2')

    with open(os.path.join(utils_dir, '__init__.py'), 'w') as f:
        pass

    with open(os.path.join(utils_dir, 'helper_functions.py'), 'w') as f:
        f.write('# Helper functions')

    with open(os.path.join(data_dir, 'raw', 'data.csv'), 'w') as f:
        pass

    # Create notebooks
    with open(os.path.join(notebooks_dir, 'exploratory_data_analysis.ipynb'), 'w') as f:
        pass

    # Create tests
    with open(os.path.join(tests_dir, 'test_module1.py'), 'w') as f:
        f.write('# Test module 1')

    with open(os.path.join(tests_dir, 'test_module2.py'), 'w') as f:
        f.write('# Test module 2')

    # Create README and requirements files if they don't exist
    readme_file = os.path.join(project_dir, 'README.md')
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as f:
            f.write(f'# {project_name}\n\nProject description goes here.')

    requirements_file = os.path.join(project_dir, 'requirements.txt')
    if not os.path.exists(requirements_file):
        with open(requirements_file, 'w') as f:
            f.write('# Required packages go here.')

    setup_file = os.path.join(project_dir, 'setup.py')
    if not os.path.exists(setup_file):
        with open(setup_file, 'w') as f:
            f.write('# Setup script goes here.')

    PROJECT_CREATED_FLAG = True


if __name__ == '__main__':
    create_project()
