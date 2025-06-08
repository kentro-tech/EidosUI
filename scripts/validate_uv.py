#!/usr/bin/env python3
"""Validate UV setup for EidosUI development."""

import sys
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run command and return success status."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    """Validate UV setup."""
    project_root = Path(__file__).parent.parent
    print(f"🔍 Validating UV setup in {project_root}")
    
    # Check if uv is installed
    success, stdout, stderr = run_command("uv --version")
    if not success:
        print("❌ UV not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh")
        return 1
    
    print(f"✅ UV found: {stdout.strip()}")
    
    # Check if pyproject.toml is valid
    print("🔄 Testing project configuration...")
    success, stdout, stderr = run_command("uv tree", cwd=project_root)
    if not success:
        print(f"❌ Project configuration test failed: {stderr}")
        print("Try running: uv sync --all-extras")
        return 1
    
    print("✅ Project configuration test passed")
    
    # Check if EidosUI can be imported (basic)
    print("🔄 Testing basic import...")
    success, stdout, stderr = run_command("python -c 'import eidos; print(\"EidosUI imported successfully\")'", cwd=project_root)
    if not success:
        print(f"❌ Import test failed: {stderr}")
        print("Try running: uv sync --all-extras")
        return 1
    
    print("✅ Import test passed")
    
    print("\n🎉 UV setup validation complete!")
    print("\nNext steps:")
    print("1. Run examples: cd examples && python basic_example.py")
    print("2. Develop: uv sync --all-extras")
    print("3. Test: uv run pytest")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 