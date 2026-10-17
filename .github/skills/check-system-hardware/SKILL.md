---
name: check-system-hardware
description: Inspects the local operating system to gather CPU details including total physical cores, logical threads, and system architecture.
---

# Check System Hardware

When asked to check hardware capabilities, CPU cores, or thread count, run the appropriate native terminal command for the user's platform to get precise details.

## Execution Steps

1. **Detect OS & Run Command**:
   - **Windows (PowerShell)**:
     ```powershell
     Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
     ```
   - **macOS**:
     ```bash
     sysctl -n hw.physicalcpu hw.logicalcpu machdep.cpu.brand_string
     ```
   - **Linux**:
     ```bash
     lscpu | grep -E 'Model name|Socket|Thread|Core|CPU\(s\)'
     ```

2. **Output Format**:
   Present the final answer clearly in a brief summary table:
   - **CPU Model Name**
   - **Physical Cores**
   - **Logical Processors / Threads**