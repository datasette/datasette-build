from datasette_build import hookimpl
import csv
import json


@hookimpl
def register_formats(register):
    register(CsvFormat(), extension="csv")
    register(CsvFormat(dialect=csv.excel_tab), extension="tsv")
    register(JsonFormat(), extension="json")


class CsvFormat:
    detect_types = True

    def __init__(self, dialect=csv.excel):
        self.dialect = dialect

    def parse_file(self, fp):
        yield from csv.DictReader(fp, dialect=self.dialect)


class JsonFormat:
    def parse_file(self, fp):
        yield from json.load(fp)
