import json, shutil, subprocess, sys
def check(name, args):
    exe=shutil.which(name)
    if not exe: return {"status":"MISSING"}
    try:
        p=subprocess.run([exe,*args],capture_output=True,text=True,timeout=8)
        return {"status":"READY" if p.returncode==0 else "UNAVAILABLE","exit_code":p.returncode}
    except (OSError,subprocess.TimeoutExpired): return {"status":"UNAVAILABLE"}
def main():
    checks={"docker_cli":check("docker",["--version"]),"docker_daemon":check("docker",["version","--format","{{.Server.Version}}"]),"compose":check("docker",["compose","version"]),"act":check("act",["--version"]),"dotnet":check("dotnet",["--version"])}
    status="READY" if all(x["status"]=="READY" for x in checks.values()) else "BLOCKED"
    print(json.dumps({"status":status,"checks":checks,"read_only":True},indent=2))
    return 0 if status=="READY" else 1
if __name__=="__main__": sys.exit(main())
