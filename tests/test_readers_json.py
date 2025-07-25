import json
import pandas as pd
from sandyie_read.readers.json_reader import read_json

def test_read_json(tmp_path):
    # Create a sample JSON file with a list of records
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
    file_path = tmp_path / "sample.json"
    file_path.write_text(json.dumps(data))

    # Use the reader function
    df = read_json(str(file_path))

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[1]["age"] == 25
