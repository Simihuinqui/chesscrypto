[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Python-CI](https://github.com/simihuinqui/chesscrypto/actions/workflows/run-tests.yml/badge.svg)](https://github.com/simihuinqui/chesscrypto/actions/workflows/run-tests.yml)
[![codecov](https://codecov.io/gh/simihuinqui/chesscrypto/branch/master/graph/badge.svg)](https://codecov.io/gh/chesscrypto/chesscrypto)
[![Documentation Status](https://readthedocs.org/projects/chesscrypto/badge/?version=latest)](http://chesscrypto.readthedocs.org/en/latest/?badge=latest)

# ChessCrypto - A Free Chess Client for Linux/Windows
Welcome to ChessCrypto, a free and feature-rich chess client designed for Linux and Windows platforms. Whether you're a beginner looking for a quick game or an advanced player seeking to enhance your skills, Ches has you covered.

## About ChessCrypto
 ChessCrypto is a GTK chess client developed primarily for GNOME but compatible with various Linux desktop environments. The entire ChessCrypto codebase, from the user interface to the chess engine, is written in Python and released under the GNU Public License.

## Goals of ChessCrypto
Provide an advanced chess client for Linux following the GNOME Human Interface Guidelines.
Offer a user-friendly interface suitable for both beginners and experienced players.
Allow users to play against the computer, find the best moves with Hint Mode, and access a range of chess engines.

## Features
ChessCrypto boasts a wide array of features to enhance your chess experience:

* Support for UCI and CECP chess engines with 8 different difficulty levels.
* Built-in Python chess engine.
* Online play on FICS (Free Internet Chess Server) with Timeseal support.
* Online play on ICC (Internet Chess Club) with timestamp support.
* Resizable chess board, "pre-drag" support, move and capture sounds, and animations.
* Compatibility with PGN, EPD, and FEN chess file formats.
* Undo, pause, and resume games.
* Various chess variants, including Atomic, Crazyhouse, Fischer Random (Chess 960), and more.
* Built-in opening book.
* Hint Mode arrows indicating the best move based on the chosen analysis engine.
* Compliance with the GNOME Human Interface Guidelines.

## Getting Started
### Installation
To install ChessCrypto, follow these steps:

* Visit the ChessCrypto Download Page on GitHub.
* Download the latest release suitable for your platform (Linux or Windows).
* Follow the installation instructions provided for your specific operating system.

### Running ChessCrypto
Once installed, you can run ChessCrypto as follows:

* Linux: Launch ChessCrypto from your application menu or execute chesscrypto in the terminal.
* Windows: Double-click the ChessCrypto executable.

### Playing Chess
* To play a game against the computer, select "New Game" and configure the options as desired.
* For online play, you can log in to FICS or ICC and enjoy games with players from around the world.

## Community and Support
* Visit the [ChessCrypto Project Homepage](https://chesscrypto.io/) for project updates and news.
* Contribute to translations on [Transifex](https://www.transifex.com/projects/p/chesscrypto/).
* Join the [ChessCrypto Mailing List](http://groups.google.com/group/chesscrypto-people) to connect with other ChessCrypto enthusiasts.
* Engage in real-time discussions on the [ChessCrypto Discord Chat](https://discord.gg/chesscrypto. 

## Contributions
ChessCrypto is an open-source project, and contributions are welcome! Whether you want to improve the code, translate the software, or help with documentation, your contributions are valued.

### How to Contribute

1. **Fork and Clone the Repository**
   - Fork the [ChessCrypto repository](https://github.com/simihuinqui/chesscrypto) to your GitHub profile.
   - Make sure you are in a directory where you are comfortable cloning the ChessCrypto project to!
   - Clone your fork from its remote repository to your local machine using:
     ```bash
     git clone https://github.com/your-username/chesscrypto.git
     cd chesscrypto
     ```

2. **Set Up Your Development Environment**
   - Ensure you have Python 3.9 or newer installed.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - If it suits your development needs, create a virtual environment to isolate your development environment:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Running ChessCrypto Locally**
   - To launch ChessCrypto, run the following command from the project root directory:
     ```bash
     python chesscrypto
     ```
   - Using the launched instance, you can monitor and reflect upon any changes you make.

4. **Understanding the Codebase**
   - The ChessCrypto repository is organized into several key directories:
     - `chesscrypto/`: Contains the core game logic and main application code.
     - `lib/`: Includes various helper libraries and associated utilities that the project depends upon.
     - `boards/`, `pieces/`: Assets and resources dealing with the chess board and pieces.
     - `docs/`: Project documentation files. Here, you can improve and contribute to other pieces of documentation.
     - `testing/`: Tests for various components of ChessCrypto.
   - Be sure to understand this organizational structure so that you can effectively contribute to it.

5. **Writing and Running Tests**
   - It is imperative to test any code you intend on deploying. Be sure to take any edge cases into account!
   - ChessCrypto uses `pytest` for testing. To run the test suite, execute:
     ```bash
     pytest
     ```
   - Any of the tests you use should be stored in testing/. This ensures adequate testing coverage of the entire project.

6. **Submitting a Pull Request**
   - When you are finished modifying the project, you can submit a pull request!
   - Create a new branch for your changes:
     ```bash
     git checkout -b feature-name
     ```
   - Add and commit your changes (be sure to use a helpful and informative message in your commit):
     ```bash
     git add .
     git commit -m "Added x, y, z"
     ```
   - Push the branch to your fork and then create a pull request to the ChessCrypto repository. Be sure to raise the PR to ChessCrypto' main branch.

7. **Review Process**
   - The managers of the ChessCrypto project will review your PR and respond accordingly.
   - Please be patient and responsive to any feedback the managers respond to you with.

### Contribution Ideas

- **Feature Enhancements**: Implement new features or improve existing ones based on user feedback or your own ideas.
- **Bug Fixes**: Look through the [issues list](https://github.com/simihuinqui/chesscrypto/issues) for bugs and try fixing them.
- **Performance Improvements**: Analyze and optimize performance-critical sections of the code.
- **Documentation**: Improve existing documentation or add new guides, tutorials, and API references.
- **Localization**: Help translate ChessCrypto into other languages via [Transifex](https://www.transifex.com/chesscrypto/chesscrypto/).

### Community and Support

- **Discussions**: Join our [ChessCrypto Discord Chat](https://discord.gg/chesscrypto) to discuss the project with other contributors and users.
- **Mailing List**: Subscribe to the [ChessCrypto Mailing List](http://chesscrypto.io/mailinglist) to stay updated on project news and announcements.
- **Report Issues**: If you encounter any bugs or have feature requests, please report them via the [GitHub Issues](https://github.com/simihuinqui/chesscrypto/issues) page.

Your contributions make ChessCrypto better for everyone. Thank you for helping us build a fantastic chess experience!

## License
ChessCrypto is released under the GNU Public License. For more details, refer to the project's License Information.
