# Sitio web — DataconsultingRRL

Sitio estático, sin dependencias externas, listo para publicar. Cuatro archivos:

| Archivo | Qué es |
|---|---|
| `index.html` | Portada: problema, soluciones con precios desde, ejemplo demostrativo, proceso, quién está detrás |
| `diagnostico.html` | Pre-diagnóstico en línea. Calcula complejidad y precio referencial, y envía la solicitud |
| `terminos.html` | Términos de uso |
| `privacidad.html` | Política de privacidad (Leyes 19.628 y 21.719) |

No usa cookies, no carga analítica ni fuentes externas, no hace llamadas a terceros. Todo el CSS
va dentro de cada archivo: se puede abrir con doble clic y funciona.

---

## Identidad visual

La paleta anterior —turquesa sobre celeste— proyectaba sector salud. La actual proyecta
tecnología y datos, que es lo que se vende.

| Uso | Color | Hex |
|---|---|---|
| Fondo principal | Azul casi negro | `#08091a` |
| Paneles y tarjetas | Azul profundo | `#141733` |
| Bordes | Índigo apagado | `#282d55` |
| **Acento principal** | Violeta eléctrico | `#7c5cff` |
| Acento claro (texto) | Violeta suave | `#9d85ff` |
| **Acento secundario** | Cian | `#22d3ee` |
| Texto sobre oscuro | Blanco azulado | `#e7e9f7` |
| Fondo de secciones claras | Gris casi blanco | `#f6f7fc` |
| Tinta sobre claro | Azul tinta | `#12142e` |

Reglas de uso:

- **Violeta → cian** es el degradado de marca. Se usa en el punto del logotipo, en la frase
  destacada del titular, en las cifras del ejemplo y en nada más. Si aparece en todas partes,
  deja de significar algo.
- **Los botones de acción** llevan degradado violeta con sombra difusa. Un solo botón primario
  por pantalla.
- **Las páginas legales van en claro**, no en oscuro: son textos largos y se leen mejor así.
  Mantienen la cabecera y el pie oscuros para no romper la continuidad.
- **Nada de turquesa ni celeste pastel.** Es lo que hacía ver el sitio como una clínica.

## Posicionamiento de IA

El sitio declara explícitamente que se usa inteligencia artificial, con una sección propia que
explica *dónde* aporta —lectura de documentos, clasificación, alertas con contexto, redacción
asistida— y tres límites que se respetan: los datos del cliente no entrenan modelos de terceros,
ninguna comunicación sale sin aprobación humana y todo lo que genera la IA queda auditable.

Esos mismos tres límites están declarados en la política de privacidad, sección 6. Si cambia la
forma en que se usa la IA, hay que actualizar ambos textos.

---

## Publicar en GitHub Pages

Ya tienes dos repositorios publicados con este flujo, así que es el camino más corto.

**1. Crear el repositorio** en GitHub con el nombre `sitio-dataconsultingrrl`.

**2. Subir los archivos:**

```bash
cd "/Users/rociorojaslacroix/Documents/Claude/Projects/Dataconsultingrrl.com/sitio-web" && git init && git add . && git commit -m "Sitio web DataconsultingRRL" && git branch -M main && git remote add origin https://github.com/rociocamilarl/sitio-dataconsultingrrl.git && git push -u origin main
```

**3. Activar Pages**: en el repositorio, `Settings` → `Pages` → Source: `Deploy from a branch`,
rama `main`, carpeta `/ (root)`. En un par de minutos queda en
`https://rociocamilarl.github.io/sitio-dataconsultingrrl/`.

**4. Verificar** que el pre-diagnóstico funciona de punta a punta antes de difundir el enlace.

---

## Apuntar el dominio propio

Hoy `dataconsultingrrl.com` tiene correo (Microsoft 365) pero **no tiene sitio**: el dominio no
resuelve a ninguna página. Para usarlo:

1. En el repositorio, `Settings` → `Pages` → `Custom domain`: escribir `dataconsultingrrl.com`.
   Esto crea un archivo `CNAME` en el repositorio.
2. En el panel DNS del proveedor donde está registrado el dominio, agregar:

| Tipo | Nombre | Valor |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | rociocamilarl.github.io |

3. **No tocar los registros MX ni TXT existentes**: son los del correo de Microsoft 365. Si se
   borran, deja de llegar el correo.
4. Esperar la propagación (minutos a algunas horas) y activar `Enforce HTTPS` en GitHub Pages.

Verificar las direcciones IP en la documentación oficial de GitHub Pages antes de cargarlas: son
las publicadas por GitHub para apex domains y podrían cambiar.

---

## Conectar el formulario a la ingesta automática

`diagnostico.html` tiene en el script la constante `FLOW_URL`, hoy vacía. Con ella vacía, el
formulario abre el correo del visitante como respaldo — que igual funciona, porque la tarea
`captura-leads-outlook-dataconsultingrrl` revisa el correo dos veces al día e ingresa los leads
sola.

Para automatizarlo del todo, ver `estado_empresa/ingesta/README.md`, sección 4.

---

## Qué revisar antes de difundir el enlace

- [ ] Los precios del sitio coinciden con `Productos Dataconsultingrrl.com/docs/matriz_precios.md`
- [ ] Términos y privacidad revisados por un abogado
- [ ] El pre-diagnóstico probado en teléfono, no solo en computador
- [ ] La solicitud de prueba llegó al correo y entró al pipeline
- [ ] Ningún texto usa el símbolo ® mientras no exista registro en INAPI
- [ ] Las cuatro páginas comparten la misma paleta y ninguna volvió al turquesa anterior
