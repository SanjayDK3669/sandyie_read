import pandas as pd
from sandyie_read.readers.csv_reader import read_csv

def test_read_csv(tmp_path):
    # Create a sample CSV file
    sample_data = "name,age\nAlice,30\nBob,25"
    file_path = tmp_path / "sample.csv"
    file_path.write_text(sample_data)

    # Read using your function
    df = read_csv(str(file_path))

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["name", "age"]
    assert df.iloc[0]["name"] == "Alice"
    assert df.iloc[1]["age"] == 25
