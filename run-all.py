touch run_all.py# run_all.py

import subprocess
import sys
import os
import time
import socket
import traceback

print("\n🚀 Booting AKWEMED Clinical AI System\n")

processes = []

# ======================================
# UTILITIES
# ======================================

def check_port(port):
    """Verifica se porta já está em uso"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0


def start_process(name, command):

    print(f"\n▶ Starting {name}")
    print(f"Command: {command}")

    try:

        process = subprocess.Popen(
            command,
            shell=True,
            stdout=sys.stdout,
            stderr=sys.stderr
        )

        processes.append(process)

        time.sleep(2)

        if process.poll() is not None:
            print(f"❌ {name} failed immediately")
        else:
            print(f"✅ {name} started successfully")

    except Exception as e:

        print(f"\n💥 ERROR starting {name}")
        print(str(e))
        traceback.print_exc()


def check_dependencies():

    print("\n🔎 Checking dependencies...")

    required = [
        "uvicorn",
        "django",
        "streamlit",
        "numpy",
        "pandas"
    ]

    missing = []

    for pkg in required:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:

        print("\n❌ Missing dependencies:")
        for m in missing:
            print(" -", m)

        print("\nInstall them with:")
        print("pip install " + " ".join(missing))

        sys.exit(1)

    print("✅ Dependencies OK")


def check_structure():

    print("\n📂 Checking project structure...")

    paths = [
        "backend/fastapi_ai/main.py",
        "manage.py",
        "apps/streamlit_lab/app.py"
    ]

    missing = []

    for p in paths:
        if not os.path.exists(p):
            missing.append(p)

    if missing:

        print("\n❌ Missing files:")
        for m in missing:
            print(" -", m)

        sys.exit(1)

    print("✅ Structure OK")


# ======================================
# MAIN
# ======================================

try:

    check_dependencies()
    check_structure()

    # ------------------------------
    # PORT CHECK
    # ------------------------------

    print("\n🌐 Checking ports...")

    ports = {
        "FastAPI": 9000,
        "Django": 8000,
        "Streamlit": 8501
    }

    for name, port in ports.items():

        if check_port(port):

            print(f"⚠ Port {port} already in use ({name})")

        else:

            print(f"✅ Port {port} available")

    # ------------------------------
    # START SERVICES
    # ------------------------------

    print("\n🧠 Starting services...\n")

    start_process(
        "FastAPI AI",
        "uvicorn backend.fastapi_ai.main:app --reload --port 9000"
    )

    start_process(
        "Django API",
        "python manage.py runserver 8000"
    )

    start_process(
        "Streamlit Dashboard",
        "streamlit run apps/streamlit_lab/app.py --server.port 8501"
    )

    # ------------------------------
    # STATUS
    # ------------------------------

    print("\n=================================")
    print("🧠 AKWEMED SYSTEM ONLINE")
    print("=================================\n")

    print("Django API   → http://127.0.0.1:8000")
    print("FastAPI AI   → http://127.0.0.1:9000/docs")
    print("Streamlit    → http://127.0.0.1:8501")

    print("\nPress CTRL+C to shutdown\n")

    # ------------------------------
    # KEEP PROCESS ALIVE
    # ------------------------------

    while True:
        time.sleep(5)

        for p in processes:

            if p.poll() is not None:

                print("\n⚠ A service stopped unexpectedly")

except KeyboardInterrupt:

    print("\n\n🛑 Shutting down services...")

    for p in processes:

        try:
            p.terminate()
        except:
            pass

    print("All services stopped")

except Exception as e:

    print("\n💥 FATAL ERROR")

    print(str(e))

    traceback.print_exc()

    for p in processes:
        try:
            p.terminate()
        except:
            pass
