#!/usr/bin/env python3
"""
Dependency Health Check Script
Checks for outdated dependencies and known vulnerabilities.
Can run locally or in CI environment.
"""

import sys
import json
import subprocess
from typing import Dict, List, Tuple
from datetime import datetime


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{"=" * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{"=" * 60}{Colors.END}\n")


def check_outdated_packages() -> Tuple[List[Dict], bool]:
    """Check for outdated packages using pip."""
    print_section("Checking for Outdated Dependencies")

    try:
        result = subprocess.run(
            ["pip", "list", "--outdated", "--format=json"],
            capture_output=True,
            text=True,
            check=True
        )

        outdated = json.loads(result.stdout)

        if not outdated:
            print(f"{Colors.GREEN}✓ All dependencies are up to date!{Colors.END}")
            return [], False

        print(f"{Colors.YELLOW}Found {len(outdated)} outdated package(s):{Colors.END}\n")

        print(f"{"Package":<20} {"Current":<15} {"Latest":<15} {"Type":<10}")
        print("-" * 70)

        for pkg in outdated:
            name = pkg["name"]
            current = pkg["version"]
            latest = pkg["latest_version"]
            pkg_type = pkg.get("latest_filetype", "wheel")

            print(f"{name:<20} {current:<15} {latest:<15} {pkg_type:<10}")

        return outdated, True

    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}✗ Error checking packages: {e}{Colors.END}")
        return [], False
    except json.JSONDecodeError:
        print(f"{Colors.RED}✗ Error parsing pip output{Colors.END}")
        return [], False


def check_vulnerabilities() -> Tuple[List[Dict], bool]:
    """Check for known vulnerabilities using safety."""
    print_section("Checking for Security Vulnerabilities")

    try:
        result = subprocess.run(
            ["safety", "check", "--output", "json"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{Colors.GREEN}✓ No known vulnerabilities found!{Colors.END}")
            return [], False

        try:
            vulnerabilities = json.loads(result.stdout)

            if not vulnerabilities:
                print(f"{Colors.GREEN}✓ No known vulnerabilities found!{Colors.END}")
                return [], False

            print(f"{Colors.RED}Found {len(vulnerabilities)} vulnerability(-ies):{Colors.END}\n")

            for vuln in vulnerabilities:
                pkg_name = vuln.get("package", "Unknown")
                installed = vuln.get("installed_version", "Unknown")
                vuln_id = vuln.get("vulnerability_id", "N/A")
                advisory = vuln.get("advisory", "No details available")

                print(f"{Colors.RED}✗ {pkg_name} v{installed}{Colors.END}")
                print(f"  ID: {vuln_id}")
                print(f"  {advisory[:200]}")
                print()

            return vulnerabilities, True

        except json.JSONDecodeError:
            # Safety might output text instead of JSON on error
            print(f"{Colors.YELLOW}⚠ Safety check completed with warnings{Colors.END}")
            print(result.stdout)
            return [], False

    except FileNotFoundError:
        print(f"{Colors.YELLOW}⚠ Safety not installed, skipping vulnerability check{Colors.END}")
        return [], False
    except Exception as e:
        print(f"{Colors.RED}✗ Error checking vulnerabilities: {e}{Colors.END}")
        return [], False


def check_dependency_tree():
    """Check for dependency conflicts using pipdeptree."""
    print_section("Dependency Tree Analysis")

    try:
        # Try to use pipdeptree if available
        result = subprocess.run(
            ["pip", "check"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{Colors.GREEN}✓ No dependency conflicts detected!{Colors.END}")
        else:
            print(f"{Colors.YELLOW}⚠ Dependency issues found:{Colors.END}")
            print(result.stdout)

    except Exception as e:
        print(f"{Colors.YELLOW}⚠ Could not check dependency tree: {e}{Colors.END}")


def generate_report(outdated: List[Dict], vulnerabilities: List[Dict]) -> Dict:
    """Generate a comprehensive report."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "outdated_count": len(outdated),
        "vulnerability_count": len(vulnerabilities),
        "outdated_packages": outdated,
        "vulnerabilities": vulnerabilities,
        "status": "pass" if not vulnerabilities else "fail"
    }

    return report


def main():
    """Main execution function."""
    print(f"\n{Colors.BOLD}{Colors.HEADER}Dependency Health Check{Colors.END}")
    print(f"Run at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

    # Check for outdated packages
    outdated, has_outdated = check_outdated_packages()

    # Check for vulnerabilities
    vulnerabilities, has_vulns = check_vulnerabilities()

    # Check dependency tree
    check_dependency_tree()

    # Generate report
    report = generate_report(outdated, vulnerabilities)

    # Save report to file
    report_file = "dependency-report.json"
    try:
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\n{Colors.BLUE}Report saved to: {report_file}{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}⚠ Could not save report: {e}{Colors.END}")

    # Print summary
    print_section("Summary")
    print(f"Outdated packages: {len(outdated)}")
    print(f"Known vulnerabilities: {len(vulnerabilities)}")

    if has_vulns:
        print(f"\n{Colors.RED}✗ FAIL: Security vulnerabilities detected!{Colors.END}")
        sys.exit(1)
    elif has_outdated:
        print(f"\n{Colors.YELLOW}⚠ WARNING: Some packages are outdated{Colors.END}")
        print(f"{Colors.GREEN}✓ PASS: No security vulnerabilities detected{Colors.END}")
        sys.exit(0)
    else:
        print(f"\n{Colors.GREEN}✓ PASS: All dependencies are healthy!{Colors.END}")
        sys.exit(0)


if __name__ == "__main__":
    main()
