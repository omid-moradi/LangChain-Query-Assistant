from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w') as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
    func=write_report,
    args_schema=WriteReportArgsSchema,
    name="write_report",
    description="write an HTML file to disk.\
        use this tool whenever someone asks for a report."
)