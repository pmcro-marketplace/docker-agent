import pathlib, json, sys
path=pathlib.Path(__file__).resolve().parents[1]/"assets"/"compose.yaml"
s=path.read_text(encoding="utf-8")
checks={"explicit_image":"OLLAMA_IMAGE:?" in s,"loopback":"127.0.0.1:11434:11434" in s,"persistent_volume":"ollama-data:/root/.ollama" in s,"no_socket":"docker.sock" not in s,"no_privileged":"privileged:" not in s}
print(json.dumps({"status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"live_validation":False},indent=2))
sys.exit(0 if all(checks.values()) else 1)
