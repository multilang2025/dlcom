"""Build data/leads/informe-leads.html from tools/leads_report_template.html + data/leads/report_data.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "tools" / "leads_report_template.html").read_text(encoding="utf-8")
data = (ROOT / "data" / "leads" / "report_data.json").read_text(encoding="utf-8")
out = tpl.replace("__DATA__", data)
(ROOT / "data" / "leads" / "informe-leads.html").write_text(out, encoding="utf-8")
print(len(out), "bytes ->", "data/leads/informe-leads.html")
