"""Instala Cloudflare Web Analytics en todas las páginas del sitio y actualiza la política de privacidad.

Uso:  python3 instalar_cloudflare_analytics.py <TOKEN>
El token sale de Cloudflare > Analytics & Logs > Web Analytics > el sitio > "Manage site" (fragmento JS).
Es un identificador público (queda visible en el código de cada página), no una clave.
Se puede ejecutar más de una vez: si la página ya tiene el código, la deja igual.
"""
import pathlib, re, sys

if len(sys.argv) != 2 or not re.fullmatch(r"[0-9a-f]{32}", sys.argv[1]):
    sys.exit("Falta el token de Cloudflare (32 caracteres hexadecimales).")
TOKEN = sys.argv[1]
RAIZ = pathlib.Path(__file__).parent
BEACON = ("<!-- Cloudflare Web Analytics: sin cookies ni datos personales -->"
          "<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
          f"data-cf-beacon='{{\"token\": \"{TOKEN}\"}}'></script>\n")

paginas = 0
for html in sorted(RAIZ.rglob("*.html")):
    t = html.read_text(encoding="utf-8")
    if "cloudflareinsights.com" in t or "</body>" not in t:
        continue
    html.write_text(t.replace("</body>", BEACON + "</body>", 1), encoding="utf-8")
    paginas += 1

pol = RAIZ / "privacidad.html"
t = pol.read_text(encoding="utf-8")
ANTES = ("No usamos cookies de seguimiento, no incorporamos\n"
         "analítica de terceros y no obtenemos datos de fuentes externas sobre ti.</p>")
DESPUES = ("No usamos cookies de seguimiento y no obtenemos datos de fuentes externas sobre ti.</p>\n"
           "<p>Para saber cuántas personas usan el sitio y qué páginas les sirven, contamos las visitas con\n"
           "Cloudflare Web Analytics. Esa medición no usa cookies, no guarda nada en tu navegador y no te\n"
           "identifica: solo entrega totales, como visitas por página, país y tipo de dispositivo.</p>")
FILA = ("  <tr>\n    <td><strong>Cloudflare</strong></td>\n"
        "    <td>Medición de visitas (Web Analytics)</td>\n"
        "    <td>Solo datos técnicos de la visita (página, país, navegador), sin cookies y sin identificarte</td>\n"
        "  </tr>\n</table>\n<p>El contenido del formulario")
if "contamos las visitas con" not in t:
    t = t.replace(ANTES, DESPUES, 1)
    t = t.replace("</table>\n<p>El contenido del formulario", FILA, 1)
    t = re.sub(r"Última actualización: [^<]*", "Última actualización: octubre de 2026", t, count=1)
    pol.write_text(t, encoding="utf-8")
    print("Política de privacidad actualizada.")
print(f"Código instalado en {paginas} páginas.")
