import pandas as pd
from myexperianepackage.simplefile import read_file, write_file, read_excel, write_excel

# Test reading and writing text files
content = "Hello, this is a test content."
write_file(r"E:\iti_python_tasks\Day_4\task_1\test.txt", content)
write_file(r"E:\iti_python_tasks\Day_4\task_1\test.txt", content)
read_content = read_file(r"E:\iti_python_tasks\Day_4\task_1\test.txt")
print("Read content:", read_content)

# Test reading and writing Excel files
data = {'Name': ['Omar', 'Essam', 'Abbas'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)
write_excel(r"E:\iti_python_tasks\Day_4\task_1\test.xlsx", df)
read_df = read_excel(r"E:\iti_python_tasks\Day_4\task_1\test.xlsx")
print("Read Excel data:\n", read_df)
