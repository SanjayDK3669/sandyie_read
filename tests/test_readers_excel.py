import pandas as pd
from sandyie_read.readers.excel_reader import read_excel

def test_read_excel(tmp_path):
    # Create a sample Excel file
    data = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [30, 25]
    })
    file_path = tmp_path / "sample.xlsx"
    data.to_excel(file_path, index=False)

    # Use the reader function
    df = read_excel(str(file_path))

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[1]["age"] == 25
