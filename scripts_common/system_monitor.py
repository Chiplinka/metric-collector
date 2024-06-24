import psutil
from datetime import datetime
import time
import requests
import argparse
import threading


def send_system_usage(url, client_id, start_time):
    # Gather CPU usage
    cpu_usage = psutil.cpu_percent()

    # Calculate RAM usage in megabytes
    vm = psutil.virtual_memory()
    ram_usage_mb = (vm.total - vm.available) / (1024 ** 2)  # Convert bytes to MB

    # Network bandwidth (bytes sent and received)
    net_io = psutil.net_io_counters()
    bandwidth_in = net_io.bytes_recv  # bytes received
    bandwidth_out = net_io.bytes_sent  # bytes sent

    # Calculate elapsed time since start
    elapsed_time = time.time() - start_time

    # Prepare the payload
    payload = {
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage_mb,
        "bandwidth_in": bandwidth_in,
        "bandwidth_out": bandwidth_out,
        "id": client_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_time": elapsed_time,
    }

    # Send the data to the server
    try:
        print("try to send", url, payload)
        response = requests.post(url, json=payload) #, timeout=5)
        print(f"Server response")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

def print_system_usage():
    # Gather CPU usage
    cpu_usage = psutil.cpu_percent()

    # Calculate RAM usage in megabytes
    vm = psutil.virtual_memory()
    ram_usage_mb = (vm.total - vm.available) / (1024 ** 2)  # Convert bytes to MB

    # Network bandwidth (bytes sent and received)
    net_io = psutil.net_io_counters()
    bandwidth_in = net_io.bytes_recv  # bytes received
    bandwidth_out = net_io.bytes_sent  # bytes sent

    start_time = time.time()

    # Calculate elapsed time since start
    elapsed_time = time.time() - start_time

    # Prepare the payload
    payload = {
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage_mb,
        "bandwidth_in": bandwidth_in,
        "bandwidth_out": bandwidth_out,
        "id": "client_id",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_time": elapsed_time,
        "opened_tabs": 0  # Include the number of opened tabs
    }

    print("--- system_monitor beginning ---\n\npayload:", payload, "\n\n--- system_monitor end ---\n")

def thread_send_system_usage(url, client_id, send_interval, start_time):
    while True:
        send_system_usage(url, client_id, start_time)
        # print_system_usage()
        time.sleep(send_interval)
    
def init_thread_send_system_usage(url, client_id, send_interval, start_time):
    monitoring_thread = threading.Thread(target=thread_send_system_usage, args=(url, client_id, send_interval, start_time))
    # monitoring_thread.daemon = True  # Set the thread as a daemon
    monitoring_thread.start()