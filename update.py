file_path = "README.md"

# 파일 읽기
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 로직: 마침표가 있으면 제거, 없으면 추가
if content.endswith("."):
    new_content = content[:-1]
else:
    new_content = content + "."

# 파일 쓰기
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)