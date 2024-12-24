# Use an Android base image
FROM ubuntu:20.04

# Install necessary tools
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk wget unzip curl git

# Set environment variables for Android SDK
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH

# Install Android SDK
RUN mkdir -p $ANDROID_HOME && \
    wget -q "https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip" -O sdk-tools.zip && \
    unzip sdk-tools.zip -d $ANDROID_HOME && \
    rm sdk-tools.zip

# Install required SDK components
RUN yes | $ANDROID_HOME/cmdline-tools/bin/sdkmanager --licenses && \
    $ANDROID_HOME/cmdline-tools/bin/sdkmanager \
    "platform-tools" \
    "platforms;android-30" \
    "system-images;android-30;google_apis;x86_64" \
    "emulator"

# Set up AVD
RUN echo "no" | $ANDROID_HOME/cmdline-tools/bin/sdkmanager --install "system-images;android-30;google_apis;x86_64" && \
    $ANDROID_HOME/emulator/emulator -avd test_avd -no-window -no-audio &

# Install Appium and Python dependencies
RUN apt-get install -y python3 python3-pip && \
    pip3 install appium pytest selenium

# Expose default Appium port
EXPOSE 4723

# Start the Appium server by default
CMD ["appium"]
