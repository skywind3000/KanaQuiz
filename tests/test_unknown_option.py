"""Focused test: unknown CLI options must be a usage error, not a silent no-op."""
import kanaquiz


def test_unknown_option_is_usage_error(tmp_path, capsys):
    kanaquiz.STORAGE = str(tmp_path / "kanaquiz")
    rc = kanaquiz.main(["kanaquiz", "-z"])
    assert rc == 2
    captured = capsys.readouterr()
    assert "unknown option" in captured.err
    assert "Traceback" not in captured.err


def test_help_still_works(tmp_path, capsys):
    kanaquiz.STORAGE = str(tmp_path / "kanaquiz")
    rc = kanaquiz.main(["kanaquiz"])
    assert rc == 0
    assert "usage" in capsys.readouterr().out
