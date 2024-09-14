# IDS706 Mini Project
![CI Status](https://github.com/YitaoS/ids706_mini_project/actions/workflows/ci.yml/badge.svg)
## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (if using DevContainer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YitaoS/ids706_mini_project.git
   cd ids706_mini_project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Optional: Build the development environment using DevContainer**:
   - Open the project in Visual Studio Code.
   - Run **Reopen in Container** from the Command Palette (`Ctrl + Shift + P` or `Cmd + Shift + P`).

### Usage

- To run the main script:
  ```bash
  python ids706_mini_project/main.py
  ```

- To run tests:
  ```bash
  make test
  ```

- To format the code:
  ```bash
  make format
  ```

- To lint the code:
  ```bash
  make lint
  ```