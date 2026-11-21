#!/usr/bin/env python3
"""Pruebas del guardián. Uso: python3 scripts/hooks/test_guardian.py"""
import datetime as dt, json, os, subprocess, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(AQUI, "guardian.py")


def correr(raiz, tool, ti, agente=None):
    d = {"tool_name": tool, "tool_input": ti, "cwd": raiz}
    if agente:
        d["agent_type"] = agente
    env = dict(os.environ, CLAUDE_PROJECT_DIR=raiz)
    out = subprocess.run([sys.executable, G], input=json.dumps(d), capture_output=True, text=True, env=env).stdout
    return "deny" if '"deny"' in out else "pasa"


def main():
    raiz = tempfile.mkdtemp()
    seg = os.path.join(raiz, "proyectos", "c1", "seguridad"); os.makedirs(seg)
    ahora = dt.datetime.now(dt.timezone.utc)
    ini, fin = (ahora - dt.timedelta(hours=1)).isoformat(), (ahora + dt.timedelta(hours=1)).isoformat()
    open(os.path.join(seg, "autorizacion-pentest.md"), "w").write(
        f"<!-- autorizacion-maquina\nestado_cliente: FIRMADA\nestado_fundador: APROBADA\n"
        f"activos: staging.c1.example\nventana_inicio: {ini}\nventana_fin: {fin}\n-->\n")
    casos = [
        ("auditor fuera de auditorias", "Write", {"file_path": "proyectos/c1/brief.md", "content": "x"}, "auditor-red-team", "deny"),
        ("auditor en auditorias", "Write", {"file_path": "auditorias/c1/fase-0-dictamen.md", "content": "x"}, "auditor-red-team", "pasa"),
        ("chief edita dictamen", "Edit", {"file_path": "auditorias/c1/fase-0-dictamen.md", "new_string": "x"}, None, "deny"),
        ("copywriter en auditorias", "Write", {"file_path": "auditorias/c1/x.md", "content": "x"}, "copywriter-conversion", "deny"),
        ("appsec su dictamen", "Write", {"file_path": "auditorias/c1/fase-4-dictamen-appsec.md", "content": "x"}, "appsec", "pasa"),
        ("appsec dictamen auditor", "Write", {"file_path": "auditorias/c1/fase-4-dictamen.md", "content": "x"}, "appsec", "deny"),
        ("bash escribe auditorias", "Bash", {"command": "echo x > auditorias/c1/a.md"}, "devops-sre", "deny"),
        ("bash lee auditorias", "Bash", {"command": "cat auditorias/c1/a.md"}, "devops-sre", "pasa"),
        ("bash sed -i auditorias", "Bash", {"command": "sed -i 's/a/b/' auditorias/c1/a.md"}, None, "deny"),
        ("bash tee auditorias", "Bash", {"command": "echo x | tee auditorias/c1/a.md"}, None, "deny"),
        ("bash rm auditorias", "Bash", {"command": "rm -rf auditorias/c1"}, None, "deny"),
        ("commit que menciona auditorias", "Bash", {"command": "git commit -m 'aísla auditorias/ <a@b.c>'"}, None, "pasa"),
        ("grep auditorias a archivo", "Bash", {"command": "grep -r x auditorias/ > /tmp/salida.txt"}, None, "pasa"),
        ("bash escribe autorizacion", "Bash", {"command": "echo x >> proyectos/c1/seguridad/autorizacion-pentest.md"}, None, "deny"),
        ("chief marca APROBADA", "Edit", {"file_path": "proyectos/c1/seguridad/autorizacion-pentest.md", "new_string": "estado_fundador: APROBADA"}, None, "deny"),
        ("chief crea plantilla", "Write", {"file_path": "proyectos/c2/seguridad/autorizacion-pentest.md", "content": "estado_fundador: PENDIENTE"}, None, "pasa"),
        ("pentest host autorizado", "Bash", {"command": "curl -sI https://staging.c1.example/login"}, "pentester-autorizado", "pasa"),
        ("pentest host tercero", "Bash", {"command": "nmap -sV api.stripe.com"}, "pentester-autorizado", "deny"),
        ("pentest mezcla hosts", "Bash", {"command": "curl https://staging.c1.example https://evil.example"}, "pentester-autorizado", "deny"),
        ("pentest sin host", "Bash", {"command": "nmap -iL objetivos"}, "pentester-autorizado", "deny"),
        ("pentest comando local", "Bash", {"command": "grep -r password proyectos/c1"}, "pentester-autorizado", "pasa"),
        ("pentest webfetch referencia", "WebFetch", {"url": "https://owasp.org/www-project-web-security-testing-guide/"}, "pentester-autorizado", "pasa"),
        ("pentest webfetch tercero", "WebFetch", {"url": "https://shop.tercero.example/"}, "pentester-autorizado", "deny"),
        ("plugin: auditor fuera", "Write", {"file_path": "proyectos/c1/brief.md", "content": "x"}, "equipo-web:auditor-red-team", "deny"),
        ("plugin: auditor dentro", "Write", {"file_path": "auditorias/c1/fase-1-dictamen.md", "content": "x"}, "equipo-web:auditor-red-team", "pasa"),
        ("plugin: pentest tercero", "Bash", {"command": "curl https://evil.example"}, "equipo-web:pentester-autorizado", "deny"),
        ("plugin: pentest autorizado", "Bash", {"command": "curl https://staging.c1.example"}, "equipo-web:pentester-autorizado", "pasa"),
        ("otro agente curl", "Bash", {"command": "curl https://example.com"}, "seo-geo", "pasa"),
    ]
    fallos = 0
    for nombre, tool, ti, ag, esperado in casos:
        r = correr(raiz, tool, ti, ag)
        ok = r == esperado
        fallos += not ok
        print(f"{'OK ' if ok else 'ERR'} {nombre}: {r} (esperado {esperado})")
    # ventana vencida
    open(os.path.join(seg, "autorizacion-pentest.md"), "w").write(
        "<!-- autorizacion-maquina\nestado_cliente: FIRMADA\nestado_fundador: APROBADA\n"
        "activos: staging.c1.example\nventana_inicio: 2020-01-01T00:00:00+00:00\nventana_fin: 2020-01-02T00:00:00+00:00\n-->\n")
    r = correr(raiz, "Bash", {"command": "curl https://staging.c1.example"}, "pentester-autorizado")
    fallos += r != "deny"
    print(f"{'OK ' if r == 'deny' else 'ERR'} pentest ventana vencida: {r} (esperado deny)")
    print(f"\n{fallos} fallos")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
