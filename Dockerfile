# Use an Ubuntu base image
FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

# Update and install required tools
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk wget unzip curl git python3 python3-pip tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip setuptools wheel && \
    pip3 install \
    appium-python-client==4.4.0 \
    pytest==7.4.0 \
    selenium==4.12.0

# Set environment variables for Android SDK
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH

# Install Android SDK Command Line Tools
RUN mkdir -p $ANDROID_HOME/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O sdk-tools.zip && \
    unzip sdk-tools.zip -d $ANDROID_HOME/cmdline-tools && \
    rm sdk-tools.zip && \
    mv $ANDROID_HOME/cmdline-tools/cmdline-tools $ANDROID_HOME/cmdline-tools/latest

# Accept Android SDK licenses and install required packages
RUN yes | sdkmanager --licenses && \
    sdkmanager --install \
    "platform-tools" \
    "platforms;android-30" \
    "system-images;android-30;google_apis;x86_64" \
    "emulator"

# Create and configure Android Virtual Device (AVD)
RUN echo "no" | avdmanager create avd -n test_avd -k "system-images;android-30;google_apis;x86_64" --device "pixel_2"

# Expose necessary ports
EXPOSE 4723

# Set working directory
WORKDIR /app

# Copy the test files to the container
COPY . /app

# Default command to start Appium server
CMD ["appium"]
