import kagglehub

# Download latest version
path = kagglehub.dataset_download("shaz13/real-world-documents-collections")

print("Path to dataset files:", path)