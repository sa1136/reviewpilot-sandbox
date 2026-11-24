from app_settings import DEFAULTS, database_url, env_overrides, load_settings, parse_bool


def test_load_settings_merges_defaults(tmp_path):
    path = tmp_path / "settings.yaml"
    path.write_text("workers: 4\n")
    settings = load_settings(str(path))
    assert settings["workers"] == 4
    assert settings["db_host"] == DEFAULTS["db_host"]


def test_parse_bool_true():
    assert parse_bool("true")


def test_env_overrides_workers(monkeypatch):
    monkeypatch.setenv("SHOP_WORKERS", "8")
    assert env_overrides(DEFAULTS)["workers"] == 8


def test_database_url(monkeypatch):
    monkeypatch.setenv("SHOP_DB_PASSWORD", "pw")
    assert database_url(DEFAULTS).startswith("postgresql://shop:")
