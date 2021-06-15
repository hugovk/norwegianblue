import norwegianblue


# pytest's capsys cannot be used in a unittest class
def test__print_verbose_print(capsys):
    # Arrange
    verbose = True

    # Act
    norwegianblue._print_verbose(verbose, "test output")

    # Assert
    captured = capsys.readouterr()
    assert captured.err == "test output\n"
