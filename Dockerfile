FROM openjdk:11-jdk

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends wget unzip npm && \
    rm -rf /var/lib/apt/lists/*

# Install Appium using npm (specify the exact version)
RUN npm install -g appium@1.22.3-4

# Set up environment variables (adjust if needed)
ENV APPIUM_HOME /usr/local/lib/node_modules/appium 
ENV PATH $APPIUM_HOME/node_modules/.bin:$PATH

# Install Python and required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install Appium-Python-Client pytest

# Download and set up Android SDK
RUN wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip && \
    unzip commandlinetools-linux-8512546_latest.zip -d android-cmdline-tools && \
    rm commandlinetools-linux-8512546_latest.zip && \
    mv android-cmdline-tools/cmdline-tools android-sdk && \
    mv android-sdk /opt/android-sdk

ENV ANDROID_HOME /opt/android-sdk
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH

# Accept Android licenses (important!)
RUN yes | sdkmanager --licenses

# Install necessary SDK components
RUN sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2" "emulator" "system-images;android-33;google_apis;x86_64"

# Create and start the Android emulator (with & disown to keep it running in background)
RUN avdmanager create avd -n test_avd -k "system-images;android-33;google_apis;x86_64" -f
RUN nohup emulator -avd test_avd -no-window -no-audio & disown

# Expose Appium port
EXPOSE 4723

# Set working directory
WORKDIR /app

# Copy the test code into the container
COPY . .

# Run the tests
CMD ["pytest", "-v"]