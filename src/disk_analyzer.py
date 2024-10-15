# src/disk_analyzer.py
import psutil
import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return {
        "total": total // (2**30),  # GB
        "used": used // (2**30),    # GB
        "free": free // (2**30)     # GB
    }

def list_partitions():
    return [part.mountpoint for part in psutil.disk_partitions()]

def analyze_disk(path="/"):
    usage = get_disk_usage(path)
    return f"Disk {path}:\nTotal: {usage['total']}GB\nUsed: {usage['used']}GB\nFree: {usage['free']}GB"

if __name__ == "__main__":
    print("Available partitions:", list_partitions())
    print(analyze_disk())