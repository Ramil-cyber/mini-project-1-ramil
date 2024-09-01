# Python GitHub Template

![Python CI](https://github.com/nogibjj/mini-project-1-ramil/actions/workflows/main.yml/badge.svg)

This repository serves as a Python project template with continuous integration (CI) setup using GitHub Actions. Additionally, it includes a **.devcontainer** configuration for streamlined development within a Docker container using Visual Studio Code.

## 🚀 Getting Started

### Local Development with VS Code and .devcontainer

Follow these steps to set up your development environment:

1. **Install Docker**: Ensure Docker is installed and running on your machine. If not, you can download it from [Docker's official website](https://www.docker.com/get-started).
2. **Install VS Code Extensions**: Install the **Remote - Containers** extension in Visual Studio Code.
3. **Clone the Repository**: Clone this repository to your local machine using the command:
    ```bash
    git clone https://github.com/nogibjj/mini-project-1-ramil.git
    ```
4. **Open in VS Code**: Open the cloned repository in Visual Studio Code.
5. **Reopen in Container**: When prompted, click on "Reopen in Container". Alternatively, you can press **F1**, type "Remote-Containers: Reopen Folder in Container", and press Enter.
6. **Docker Image Build**: The first time you open the project in the container, Docker will build the image as specified in the **Dockerfile**. This may take a few minutes.
7. **Ready-to-Use Environment**: After the setup is complete, you will have a fully configured Python development environment isolated from your local system.

### 🧪 Running Tests

To run tests and ensure your code is working as expected:

1. **Navigate to the Project Directory**: Open a terminal within VS Code (you should already be in the correct directory if you followed the previous steps).
2. **Run Tests**: Execute the following command to run all unit tests:
    ```bash
    pytest
    ```
3. **Review Results**: Check the test output to ensure no new issues were introduced by your changes.

### 📦 Installation of Dependencies

If you need to install or update dependencies:

1. **Edit `requirements.txt`**: Add any new Python packages you need.
2. **Install Dependencies**: Run the following command inside the container:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ File Structure

This project is organized as follows:

- **`src/main.py`**: Contains the primary function `greet`, which returns a greeting message.
- **`tests/test_main.py`**: Includes unit tests for the `greet` function.
- **`requirements.txt`**: Specifies the Python dependencies required for this project.
- **`.devcontainer/`**: Holds configurations for the VS Code remote container development environment.
- **`.github/workflows/main.yml`**: Defines workflows for Continuous Integration using GitHub Actions.

## ✨ Contributing

We welcome contributions to this project! Please follow these steps to contribute:

1. **Fork the Repository**: Click on the "Fork" button at the top of the repository page.
2. **Create a New Branch**: Create a new branch for your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make Your Changes**: Implement your changes and commit them to your branch.
4. **Run Tests**: Ensure all tests pass by running `pytest`:
    ```bash
    pytest
    ```
5. **Submit a Pull Request**: Push your changes to your fork and open a pull request with a detailed description of your modifications.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Pushing Changes to the Repository

Once you’ve made changes to the README or other files, follow these steps to push them to GitHub:

1. **Add Changes**: Stage your changes using:
    ```bash
    git add .
    ```
2. **Commit Changes**: Commit your staged changes with a meaningful message:
    ```bash
    git commit -m "Updated README with enhanced instructions"
    ```
3. **Push Changes**: Push your changes to the main branch:
    ```bash
    git push -u origin main
    ```
