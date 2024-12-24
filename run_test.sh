#!/bin/bash

# Build the Docker image
docker build -t android-test-runner .

# Run the Docker container with the necessary ports and volumes
docker run --rm -it \
    -p 4723:4723 \
    -v "$(pwd)/tests:/tests" \
    android-test-runner bash -c "
    emulator @test_avd -no-audio -no-window &
    sleep 20 &&
    pytest /tests --maxfail=1 --disable-warnings
    "
