from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from pathlib import Path
import csv


class TestPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Processing csv.")

        input_csv = input_data.input_csv
        
        """Reads a CSV file and returns its content as a list of lists."""
        data_list = []
        with open(input_csv, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)

        # Return list of items in csv
        return OutputModel(output_value=data_list)
