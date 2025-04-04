#!/bin/bash
cd "$(dirname "$0")"

# === CONFIG ===
CPP_DIR="cpp"
CPP_FILE="main.cpp"
CPP_OUT="main.out"
BUILD="build"
PY_FILE="main.py"

# === BUILD C++ ===
echo "🔧 Building C++..."
g++ "$CPP_DIR/$CPP_FILE" -std=c++17 -o "$BUILD/$CPP_OUT"

# Check if build succeeded
if [ $? -ne 0 ]; then
    echo "❌ C++ build failed!"
    exit 1
fi

echo "✅ C++ build succeeded."

# === RUN Python Script ===
echo "🚀 Running Python script..."
python3 "$PY_FILE"