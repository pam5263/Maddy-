# MagxxicVOT SMS Tool

A comprehensive bulk SMS sending tool supporting multiple providers.

## Features
- Support for Twilio, Vonage (Nexmo), Plivo, Messagebird, Telnyx, Telesign, and AWS SNS.
- Proxy rotation (SOCKS5).
- Link tracking and shortening via TinyURL.
- Phone number generation and carrier filtering.
- HWID-based license activation.

## Installation
1. Install dependencies:
   - **Windows**: Double-click `setup.bat`
   - **Linux/macOS**: `pip install -r requirements.txt`

> **Note**: If you encounter `ModuleNotFoundError: No module named 'pkg_resources'`, it means `setuptools` is missing. Running `setup.bat` (Windows) or `pip install setuptools` (Linux/macOS) will fix this.

## Setup
1. **License Activation**:
   - Run `python3 sms_tool.py`.
   - Copy your System Token.
   - Run `python3 generate_key.py <TOKEN>` to get your Activation Key.
   - Create a file named `license.key` and paste the key.
2. **API Key Configuration**:
   There are two ways to provide your API keys:

   **Option A: Edit `credentials.env` (Recommended)**
   - Open `credentials.env` in a text editor (like Notepad).
   - Enter your keys after the `=` sign for each provider.
   - Example: `TWILIO_ACCOUNT_SID=your_sid_here`
   - Save the file and restart the tool.

   **Option B: Environment Variables**
   Set the following environment variables on your system:
   - `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`
   - `VONAGE_API_KEY`, `VONAGE_API_SECRET`, `VONAGE_PHONE_NUMBER`
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION_NAME`
   - `PLIVO_AUTH_ID`, `PLIVO_AUTH_TOKEN`, `PLIVO_PHONE_NUMBER`
   - `MESSAGEBIRD_API_KEY`, `MESSAGEBIRD_PHONE_NUMBER`
   - `TELNYX_API_KEY`, `TELNYX_PHONE_NUMBER`
   - `TELESIGN_CUSTOMER_ID` (or `TELESIGN_AUTH_ID`), `TELESIGN_API_KEY` (or `TELESIGN_AUTH_TOKEN`), `TELESIGN_PHONE_NUMBER`
   - `TEXTBELT_API_KEY`

## Troubleshooting

### "Invalid base64-encoded string" (Telesign)
This error means your **Telesign API Key** is incorrect or incomplete.
- Telesign API keys are exactly **88 characters** long and usually end with `==`.
- Ensure you copied the entire string from the Telesign dashboard into `credentials.env`.
- If the tool reports a length other than 88 during startup, you have a copy-paste error.

## Usage
- Run the tool:
  - **Windows**: Double-click `start.bat`
  - **Linux/macOS**: `python3 sms_tool.py`
- Follow the on-screen menu instructions.
- Load numbers from `numbers.txt` and proxies from `proxies.txt`.
