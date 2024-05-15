pytest_plugins = ["plugins.tools_plugin"]


def pytest_configure(config):
    config.addinivalue_line("markers", "db_test: mark test as a database test.")
