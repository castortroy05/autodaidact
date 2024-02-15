#!/bin/bash

# Create the directory structure
mkdir -p autodaidact/autolearn/envs
mkdir -p autodaidact/autolearn/agents
mkdir -p autodaidact/autolearn/models
mkdir -p autodaidact/autolearn/utils
mkdir -p autodaidact/tests
mkdir -p autodaidact/scripts

# Create __init__.py files to make Python treat the directories as packages/modules
touch autodaidact/autolearn/__init__.py
touch autodaidact/autolearn/envs/__init__.py
touch autodaidact/autolearn/agents/__init__.py
touch autodaidact/autolearn/models/__init__.py
touch autodaidact/autolearn/utils/__init__.py
touch autodaidact/tests/__init__.py

# Create placeholder files for base agent, example model, helper functions, test cases, and training script
touch autodaidact/autolearn/agents/base_agent.py
touch autodaidact/autolearn/models/example_model.py
touch autodaidact/autolearn/utils/helpers.py
touch autodaidact/tests/test_envs.py
touch autodaidact/scripts/train_agent.py

# Create README.md, requirements.txt, and setup.py at the root of the project
touch autodaidact/README.md
touch autodaidact/requirements.txt
touch autodaidact/setup.py

# Move the existing autolearn_env.py to the new structure
# Ensure that the path to autolearn_env.py is correct relative to where this script is run
mv autolearn_env.py autodaidact/autolearn/envs/

echo "Project structure for autodaidact created successfully."
