import os
from pathlib import Path

project_name = "ai_interview_assistant"

list_of_files = [
    f"{project_name}/app.py",
    f"{project_name}/template.py",
    f"{project_name}/pages/1_setup.py",
    f"{project_name}/pages/2_interview.py",
    f"{project_name}/pages/3_coding.py",
    f"{project_name}/pages/4_dashboard.py",
    f"{project_name}/llm_engine.py",
    f"{project_name}/voice_module.py",
    f"{project_name}/analytics.py",
    f"{project_name}/utils.py",
    f"{project_name}/data/interview_logs.db",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create empty files if not present
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File already present at: {filepath}")

print("✅ Demo project structure created successfully!")
