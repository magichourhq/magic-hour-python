from codemod.populate_custom_docs import CustomDocsPopulator


def test_append_generate_parameters_adds_missing_comma() -> None:
    create_call = """client.v1.face_detection.generate(
    assets={"target_file_path": "/path/to/1234.png"}, confidence_score=0.5"""
    generate_params = (
        "wait_for_completion=True,\n"
        "    download_outputs=True,\n"
        '    download_directory="."'
    )

    result = CustomDocsPopulator._append_generate_parameters(
        create_call, generate_params
    )

    assert "confidence_score=0.5,\n    wait_for_completion=True" in result
    assert result.endswith('\n    download_directory="."\n)')


def test_append_generate_parameters_preserves_existing_comma() -> None:
    create_call = """client.v1.ai_image_generator.generate(
    style={"prompt": "A sunset"},"""

    result = CustomDocsPopulator._append_generate_parameters(
        create_call, "wait_for_completion=True,"
    )

    assert "style={\"prompt\": \"A sunset\"},,\n" not in result
    assert "style={\"prompt\": \"A sunset\"},\n" in result
