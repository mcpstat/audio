import streamlit as st
import sounddevice as sd

def list_audio_devices():
    devices = sd.query_devices()
    return devices

def main():
    st.title("Audio Device Checker")

    st.write("Checking available audio devices...")

    devices = list_audio_devices()

    if devices:
        st.write("Available audio devices:")
        for i, device in enumerate(devices):
            st.write(f"Device {i}: {device['name']}, Input Channels: {device['max_input_channels']}, Output Channels: {device['max_output_channels']}")
    else:
        st.write("No audio devices found.")

if __name__ == "__main__":
    main()
