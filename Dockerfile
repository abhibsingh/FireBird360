# Use an Android base image
FROM ubuntu:20.04

# Set environment variables to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

# Install necessary tools
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk wget unzip curl git python3 python3-pip tzdata && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Set environment variables for Android SDK
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH

# Install Android SDK
RUN mkdir -p $ANDROID_HOME && \
    wget -q "https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip" -O sdk-tools.zip && \
    unzip sdk-tools.zip -d $ANDROID_HOME && \
    rm sdk-tools.zip && \
    yes | $ANDROID_HOME/cmdline-tools/bin/sdkmanager --licenses && \
    $ANDROID_HOME/cmdline-tools/bin/sdkmanager \
    "platform-tools" \
    "platforms;android-30" \
    "system-images;android-30;google_apis;x86_64" \
    "emulator"

# Install Python dependencies
RUN pip3 install appium pytest selenium

# Create and configure an Android emulator
RUN echo "no" | $ANDROID_HOME/emulator/emulator -avd test_avd -no-audio -no-window || true && \
    $ANDROID_HOME/cmdline-tools/bin/sdkmanager --install emulator

# Expose Appium port
EXPOSE 4723

# Set the working directory
WORKDIR /app

# Copy test files into the container
COPY . /app

# Default command to start Appium server
CMD ["appium"]
