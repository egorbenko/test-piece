from domino.testing import piece_dry_run
from pathlib import Path

csv_file = str(Path(__file__).parent / "test.csv")

def test_test_piece():
    input_data = dict(
        input_csv = csv_file
    )
    output_data = piece_dry_run(
        piece_name="TestPiece",
        input_data=input_data
    )

    assert output_data is not None
    assert len(output_data["output_value"]) == 2