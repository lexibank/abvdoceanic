def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


# should be 210 items
def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 210


# test we have some languages
def test_languages(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) > 1000


# test we have some cognates
def test_cognates(cldf_dataset):
    assert len(list(cldf_dataset["CognateTable"])) == 233260
