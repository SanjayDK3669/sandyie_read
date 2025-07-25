from sandyie_read.readers.js_reader import read_js

def test_read_js(tmp_path):
    # Create a sample JS file
    js_code = "function greet() { console.log('Hello, world!'); }"
    file_path = tmp_path / "sample.js"
    file_path.write_text(js_code)

    # Read using your reader
    content = read_js(str(file_path))

    # Assertions
    assert isinstance(content, str)
    assert "function greet()" in content
    assert "console.log('Hello, world!');" in content
