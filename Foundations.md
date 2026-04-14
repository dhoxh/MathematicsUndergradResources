
This section walks through installing every tool used in this guide. Complete these steps before moving into any other section. The goal is to get everything installed and confirmed working so that later sections can focus entirely on how to use these tools for mathematics — not on troubleshooting installations.

Work through the installations in the order listed. Some tools depend on others (for example, NumPy and Matplotlib require Python), so the sequence matters.

---

## Table of Contents

1. [Git](#1-git)
2. [Python](#2-python)
3. [NumPy](#3-numpy)
4. [Matplotlib](#4-matplotlib)
5. [R and RStudio](#5-r-and-rstudio)
6. [Obsidian](#6-obsidian)
7. [Confirming Your Setup](#7-confirming-your-setup)

---

## 1. Git

**What it is:** Git is a version control system that tracks changes to your files over time. You will use it to back up your LaTeX files, R scripts, and Python scripts to GitHub so your work is never lost and is accessible from any machine. File sync servers are sometimes slow and require a strong internet connection. With git you can get by with a relatively weak connection and a simple terminal

**Installation:**

### macOS

macOS often comes with Git pre-installed. To check, open Terminal and run:

```bash
git --version
```

If a version number appears, Git is already installed. If not, macOS will prompt you to install Xcode Command Line Tools — follow that prompt.

Alternatively, install Git via Homebrew (recommended if you plan to use other developer tools):

```bash
brew install git
```

### Windows

Download the installer from the official site:

> https://git-scm.com/download/win

Run the installer. When prompted about the default editor, select your preferred text editor (VS Code is a safe choice). Leave all other options at their defaults.

After installation, open **Git Bash** (installed alongside Git) and run:

```bash
git --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

**First-time configuration:**

After installing, tell Git who you are. Run these two commands in your terminal, replacing the placeholders with your own name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

This information is attached to every commit you make. Use the same email associated with your GitHub account.

---

## 2. Python

**What it is:** Python is the programming language used to run NumPy and Matplotlib. This guide recommends installing Python through **Anaconda**, a distribution that bundles Python with a package manager and many scientific libraries pre-installed — including NumPy and Matplotlib.

**Installation via Anaconda (recommended):**

Download the Anaconda Individual Edition installer for your operating system:

> https://www.anaconda.com/download

Run the installer and follow the on-screen instructions. When asked whether to add Anaconda to your PATH, select **yes** if you are on Windows. On macOS or Linux, the installer handles this automatically.

After installation, open a new terminal window and confirm Python is available:

```bash
python --version
```

You should see something like `Python 3.11.x` or similar. If you see `Python 2.x`, run `python3 --version` instead — your system may have an older Python 2 installation alongside the new one.

**Why Anaconda over a standalone Python install:** Anaconda installs `conda`, a package manager that handles dependencies more reliably than `pip` alone for scientific packages. It also installs Jupyter Notebook, which provides a browser-based interface for running Python code interactively — useful for testing NumPy and Matplotlib code alongside your math work.

---

## 3. NumPy

**What it is:** NumPy is the Python library for numerical computation. It is included by default with Anaconda. If you installed Python through Anaconda, NumPy is already available.

**Verify the installation:**

Open a terminal and run:

```bash
python -c "import numpy; print(numpy.__version__)"
```

If a version number prints (e.g., `1.26.0`), NumPy is ready.

**If NumPy is not installed** (for example, if you installed Python without Anaconda):

```bash
pip install numpy
```

Or, if using conda:

```bash
conda install numpy
```

---

## 4. Matplotlib

**What it is:** Matplotlib is the Python library for creating graphs and visualizations. Like NumPy, it is included with Anaconda.

**Verify the installation:**

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

**If Matplotlib is not installed:**

```bash
pip install matplotlib
```

Or with conda:

```bash
conda install matplotlib
```

**Quick test — generate your first plot:**

Run the following in a terminal or Jupyter Notebook to confirm Matplotlib is working correctly:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
```

A window displaying a sine curve should appear. If it does, your Python environment — including NumPy and Matplotlib — is fully operational.

---

## 5. R and RStudio

**What it is:** R is a programming language for statistical computing. RStudio is a free interface (called an IDE) that makes R significantly easier to use by providing a console, script editor, and output pane in one window. Install both.

**Step 1 — Install R:**

Download R from CRAN (the Comprehensive R Archive Network):

> https://cran.r-project.org

Select your operating system and follow the instructions. Always install the most recent release.

**Step 2 — Install RStudio:**

Download the free RStudio Desktop version from Posit:

> https://posit.co/download/rstudio-desktop/

Install RStudio after R is already installed. RStudio detects R automatically.

**Verify the installation:**

Open RStudio. In the console panel (bottom left), run:

```r
R.version.string
```

A version string for your R installation should print. You are now ready to use R.

**Install a starter package:**

From the RStudio console, install `ggplot2`, which you will use for visualization:

```r
install.packages("ggplot2")
```

R will download and install the package. When it finishes, confirm it works:

```r
library(ggplot2)
```

No error message means the package loaded successfully.

---

## 6. Obsidian

**What it is:** Obsidian is a note-taking application that stores your notes as plain Markdown files on your own machine. You will use it to build a connected knowledge base of definitions, theorems, and proofs that links related concepts across courses.

**Installation:**

Download Obsidian for your operating system:

> https://obsidian.md/download

Run the installer. Obsidian requires no account and no internet connection to use.

**Create your first vault:**

A vault is a folder that Obsidian uses to store all your notes. When Obsidian opens for the first time:

1. Select **Create new vault**
2. Name it something like `Math Notes` or `Undergraduate Vault`
3. Choose a location you will remember — your Documents folder is a reasonable default
4. Click **Create**

Obsidian opens to an empty vault. You are ready to create notes.

**Install the recommended plugins:**

Obsidian supports community-built plugins that extend its functionality. To install them:

1. Open **Settings** (gear icon, bottom left)
2. Go to **Community plugins**
3. Turn off **Safe mode** when prompted
4. Click **Browse** and search for each plugin below

| Plugin          | Purpose                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **LaTeX Suite** | Expands snippets for typing math notation quickly (e.g., type `mk` to enter inline math mode)       |
| **Dataview**    | Lets you query your notes like a database — useful for building indexes of definitions and theorems |
| Git             | Let's you control git content directly in obsidian with an easy to use GUI                          |

To install a plugin: click it in the browse panel, click **Install**, then click **Enable**.

**Connect your vault to GitHub (optional but recommended):**

Backing up your Obsidian vault to GitHub ensures your notes are never tied to a single machine. To do this, navigate to your vault's folder in a terminal and initialize a Git repository:

```bash
cd path/to/your/vault
git init
git remote add origin https://github.com/yourusername/your-repo-name.git
```

From that point forward, commit and push changes after each study session to keep your backup current. Alternatively, obsidian comes with a community plugin that handles all of this for you

---

## 7. Confirming Your Setup

Run through this checklist before moving to any other section of the guide. Each check should take less than a minute.

|Tool|Confirmation Command|Expected Output|
|---|---|---|
|Git|`git --version`|`git version 2.x.x`|
|Python|`python --version`|`Python 3.x.x`|
|NumPy|`python -c "import numpy; print(numpy.__version__)"`|A version number|
|Matplotlib|`python -c "import matplotlib; print(matplotlib.__version__)"`|A version number|
|R|Run `R.version.string` in RStudio console|An R version string|
|Obsidian|Open the application|Vault loads without error|

If any check fails, return to that tool's section above and re-read the installation steps. The most common issues are:

- **Python not found:** Close and reopen your terminal after installing Anaconda — the terminal needs to reload to recognize the new installation.
- **NumPy or Matplotlib import error:** Confirm you are running the same Python that Anaconda installed. Type `which python` (macOS/Linux) or `where python` (Windows) to see which Python your terminal is using.
- **R not found in RStudio:** Reinstall RStudio after confirming R is installed. RStudio must detect R during its own installation.

Once every item in the checklist is confirmed, your environment is ready. Proceed to the next section.