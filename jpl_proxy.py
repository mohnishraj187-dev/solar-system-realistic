from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlencode, urlparse, parse_qs
from urllib.request import urlopen
from pathlib import Path

ROOT = Path(__file__).parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/jpl-body"):
            target = parse_qs(urlparse(self.path).query).get("target", ["399"])[0]
            query = urlencode({
                "format": "text", "COMMAND": "'" + target + "'", "OBJ_DATA": "'NO'",
                "MAKE_EPHEM": "'YES'", "EPHEM_TYPE": "'VECTORS'", "CENTER": "'500@10'",
                "START_TIME": "'2026-09-26'", "STOP_TIME": "'2026-09-27'",
                "STEP_SIZE": "'1d'", "OUT_UNITS": "'AU-D'", "REF_PLANE": "'ECLIPTIC'",
                "REF_SYSTEM": "'J2000'", "VEC_TABLE": "'2'", "CSV_FORMAT": "'YES'",
            })
            try:
                with urlopen("https://ssd.jpl.nasa.gov/api/horizons.api?" + query, timeout=20) as response:
                    data = response.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)
            except Exception as exc:
                self.send_error(502, str(exc))
            return
        super().do_GET()

print("Solar System Realistic Data Lab running at http://localhost:8001")
ThreadingHTTPServer(("127.0.0.1", 8001), Handler).serve_forever()
