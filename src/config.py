# Workspace configuration file# Workspace contion file
"""
ZAV-1 FLIGHT CONTROL SYSTEM | CONFIGURATION MODULE
----------------------------------------------------
- ARCHITECTURE: DEBIAN / HYPRLAND / NEXT.JS
- HARDWARE: BMP280, ARDUINO-COMPATIBLE
- VERSION: 1.0.0-STABLE
----------------------------------------------------
"""

# --- SYSTEM IDENTIFIERS ---
DEVICE_NAME = "ZAV-1_CORE"
FIRMWARE_VER = "2026.07.18"
DEBUG_MODE = True
LOG_LEVEL = "VERBOSE"

# --- I2C / HARDWARE BUS CONFIGURATION ---
# BMP280 Address and bus definition
I2C_BUS_PRIMARY = 1
BMP280_ADDR = 0x76
PRESSURE_OVERSAMPLING = 2
TEMPERATURE_OVERSAMPLING = 2
FILTER_COEFFICIENT = 4

# --- FLIGHT DYNAMICS & PID CONSTANTS ---
# P = Proportional, I = Integral, D = Derivative
# Tuning values for the ZAV-1 airframe
PID_ROLL_P = 0.15
PID_ROLL_I = 0.01
PID_ROLL_D = 0.05

PID_PITCH_P = 0.12
PID_PITCH_I = 0.01
PID_PITCH_D = 0.04

PID_YAW_P = 0.20
PID_YAW_I = 0.02
PID_YAW_D = 0.08

# --- TELEMETRY THRESHOLDS ---
MAX_ALTITUDE_METERS = 500.0
CRITICAL_ALTITUDE_METERS = 450.0
MIN_BATTERY_VOLTAGE = 3.4
CRITICAL_BATTERY_VOLTAGE = 3.2

# --- SENSOR SAMPLING INTERVALS (in seconds) ---
SAMPLE_RATE_FAST = 0.01
SAMPLE_RATE_SLOW = 0.1
DATA_SYNC_INTERVAL = 0.5

# --- PIN MAPPING (GPIO / ARDUINO) ---
PIN_LED_STATUS = 13
PIN_BUZZER = 12
PIN_ARMING_SWITCH = 11
PIN_PWM_THROTTLE = 9

# --- OPERATIONAL MODES ---
MODE_MANUAL = 0x01
MODE_STABILIZED = 0x02
MODE_AUTONOMOUS = 0x04
MODE_EMERGENCY_LAND = 0x08

# --- COMMUNICATION SETTINGS ---
BAUD_RATE = 115200
SERIAL_TIMEOUT = 0.05
BUFFER_SIZE = 1024

# --- SAFETY LOGIC ---
FAILSAFE_TIMEOUT = 2.0  # Seconds before auto-land on signal loss
MAX_TILT_ANGLE = 45.0  # Degrees
MAX_ACCEL_G = 4.0      # G-force threshold

# --- STORAGE & PATHS ---
LOG_DIRECTORY = "/var/log/zav1/"
DATA_STORE_PATH = "/home/alaaabbadi/zav1-data/"
DB_NAME = "telemetry.sqlite"

# --- CALIBRATION OFFSETS ---
# Adjust based on bench testing
GYRO_OFFSET_X = 0.02
GYRO_OFFSET_Y = -0.01
GYRO_OFFSET_Z = 0.00
ACCEL_OFFSET_Z = 9.81

# --- POST-FLIGHT LOGGING ---
ENABLE_AUTO_EXPORT = True
EXPORT_FORMAT = "JSON"
RETAIN_LOGS_DAYS = 7

# --- END OF CONFIG ---
def get_config_summary():
    """
    Returns a dictionary of core flight parameters 
    for the GUI/Telemetry dashboard.
    """
    return {
        "device": DEVICE_NAME,
        "firmware": FIRMWARE_VER,
        "mode": MODE_STABILIZED,
        "safety_limit": MAX_TILT_ANGLE
    }

# EOF