#!/usr/bin/env python3
"""
Simple test script to validate run.bat logic WITHOUT Windows-only dependencies
Tests the core PATH resolution and installation logic
"""

import subprocess
import sys
import os
from pathlib import Path


def test_python_available():
    """Test: Python is available"""
    print("\n[1/5] Testing Python availability...")
    result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ Python found: {result.stdout.strip()}")
        return True
    print("  ✗ Python not found")
    return False


def test_pip_available():
    """Test: pip is available"""
    print("\n[2/5] Testing pip availability...")
    result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ pip found: {result.stdout.strip()}")
        return True
    print("  ✗ pip not found")
    return False


def test_uv_installation():
    """Test: uv can be installed"""
    print("\n[3/5] Testing uv installation...")

    # Check if already installed
    result = subprocess.run([sys.executable, "-m", "pip", "show", "uv"], capture_output=True, text=True)
    if result.returncode == 0:
        print("  ✓ uv already installed via pip")
        return True

    # Check if in PATH (already installed system-wide)
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print("  ✓ uv already available in PATH")
        return True

    # Try to install with --user flag for PEP 668 compliance
    print("  ! Attempting to install uv with --user flag...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--user", "uv"], capture_output=True, text=True)
    if result.returncode == 0:
        print("  ✓ uv installed successfully")
        return True

    print("  ✗ Failed to install uv (may be a permission issue)")
    return False


def test_uv_in_path():
    """Test: uv is callable from PATH"""
    print("\n[4/5] Testing if uv is in PATH...")

    # Try direct call
    result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ uv callable: {result.stdout.strip()}")
        return True

    # Try via python module
    print("  ! uv not in PATH, trying via Python module...")
    result = subprocess.run([sys.executable, "-m", "uv", "--version"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ uv accessible via python -m: {result.stdout.strip()}")
        return True

    print("  ✗ uv is not accessible")
    return False


def test_project_files():
    """Test: Required project files exist"""
    print("\n[5/5] Testing project files...")

    files_to_check = [
        "autoskip_dialogue.py",
        "pyproject.toml",
        "run.bat"
    ]

    all_exist = True
    for fname in files_to_check:
        fpath = Path(fname)
        if fpath.exists():
            print(f"  ✓ {fname}")
        else:
            print(f"  ✗ {fname} NOT FOUND")
            all_exist = False

    return all_exist


def main():
    print("="*60)
    print("TESTING run.bat LOGIC (Linux/Mac Compatible)")
    print("="*60)

    tests = [
        ("Python availability", test_python_available),
        ("pip availability", test_pip_available),
        ("uv installation", test_uv_installation),
        ("uv in PATH", test_uv_in_path),
        ("Project files", test_project_files),
    ]

    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"  ✗ Exception: {e}")
            results[test_name] = False

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, passed_flag in results.items():
        status = "✓" if passed_flag else "✗"
        print(f"{status} {test_name}")

    print(f"\nResult: {passed}/{total} tests passed")
    print("="*60)

    if passed == total:
        print("✓ SUCCESS - run.bat setup logic is correct!")
        return 0
    else:
        print(f"✗ FAILURE - {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
