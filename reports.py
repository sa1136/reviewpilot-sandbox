"""Stock report export."""

import subprocess


def report_rows(levels: dict[str, int]) -> list[tuple[str, int]]:
    """Rows for the stock report, sorted by SKU."""
    return sorted(levels.items())


def export_report(report_name: str) -> None:
    """Compress the named report into the exports folder."""
    command = f"tar -czf exports/{report_name}.tgz reports/{report_name}.csv"
    subprocess.run(command, shell=True, check=True)
