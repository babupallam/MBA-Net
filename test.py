import os

# Define the root directory for the repository
repo_name = "MBA-Net"
clip_branch = "clip-implementation"
base_path = os.path.join(repo_name, clip_branch)

# Define the structure
folders = [
    f"{base_path}/.venv",
    f"{base_path}/doc_images",
    f"{base_path}/model",
    f"{base_path}/data_utils",
    f"{base_path}/experiments",
    f"{base_path}/utils"
]

files = [
    f"{base_path}/model/__init__.py",
    f"{base_path}/model/MBA_modules.py",
    f"{base_path}/model/clip_backbone.py",          # New: CLIP backbone integration
    f"{base_path}/model/clip_mba_net.py",           # New: CLIP model without attention
    f"{base_path}/model/clip_mba_net_attention.py", # New: CLIP model with attention

    f"{base_path}/data_utils/__init__.py",
    f"{base_path}/data_utils/clip_dataset.py",      # New: Dataset handling with CLIP
    f"{base_path}/data_utils/preprocess.py",        # New: Image preprocessing for CLIP

    f"{base_path}/experiments/clip_config_no_attention.yaml", # CLIP without attention
    f"{base_path}/experiments/clip_config_attention.yaml",    # CLIP with attention

    f"{base_path}/utils/__init__.py",
    f"{base_path}/utils/lr_scheduler.py",           # Existing moved here
    f"{base_path}/utils/random_erasing.py",         # Existing moved here
    f"{base_path}/utils/evaluation_metrics.py",     # Existing moved here

    f"{base_path}/train_clip.py",                   # New: Training script for CLIP models
    f"{base_path}/eval_clip.py",                    # New: Evaluation script for CLIP models
    f"{base_path}/requirements.txt",
    f"{base_path}/README_CLIP.md"                   # New: Documentation for CLIP branch
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass  # Just create the file

print(f"Repository structure for '{clip_branch}' branch created successfully! ✅")
