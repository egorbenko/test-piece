from pydantic import BaseModel, Field


class InputModel(BaseModel):
    input_csv: str = Field(
        description='Input csv. It should be either a path to a file, or a base64 encoded string.',
        json_schema_extra={
            "from_upstream": "always"
        }
    )

class OutputModel(BaseModel):
    output_value: list = Field(
        description='output array'
    )
