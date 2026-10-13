import os
files_count = 0
for root,dirs,files in os.walk(r"E:\项目学习"):
    dirs[:] = [d for d in dirs if d not in [".git", "_ref", "_备份", "__pycache__", ".idea",'.claude', '.playwright-mcp']]
    files_count += len(files)
print(files_count)

