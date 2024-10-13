# Onslow College Digital Technologies

## Programming Template

Use this template to develop a program in Swift 6 on a Linux host.

## Actions

![Action buttons](.devcontainer/actions.jpg)

- ▶️ **Build and Run**: build and run the code in the `Sources` folder
- ✏️ **Format**: on first click, installs swift-format. After that, reformats your code
- 🖥️ **New Terminal**: open a terminal window to run a Linux command
- 🗑️ **Kill All Terminals**: closes all terminal windows
- 👁️ **Kaiako Mode**: makes the text larger so your kaiako can read your code more easily on your computer

## Starting new projects

When you create new projects, you must **create a new branch**. Create a branch per project based on the `main` branch.

1. At the bottom of the window, click on the **Source Control** button (between the Codespaces button and the refresh icon)
2. At the top of the screen, click on **Create new branch from…**, then click `origin/main`
3. Type a meaningful name for your branch. For example, `loops` or `task2`.
   - Don't include spaces, symbols (aside from dashes or underscores), or capital letters in the name

## Switch to another project

1. At the bottom of the window, click on the **Source Control** button.
2. Click on your previous project.
   - If you receive an error, you may need to wait until all your changes in your current branch have been committed and pushed first.

## Adding project dependencies

You can add libraries/frameworks written by other developers. For example, you can write code to  

1. Open the `Package.swift` file
2. Add your dependency line to the `dependencies` array.
   ```swift
   dependencies: [
      .package(url: "https://github.com/owner/MyDependency.git", from: "1.0.0")
   ]
   ```
3. Add the dependency to the `dependencies` array in the `targets`.
   ```swift
   .executableTarget(
      name: "Program",
      dependencies: [
         "MyDependency",
      ]
   )
   ```
4. Save the file. Swift will detect the changes and automatically download the new package; you will then be able to import the package in your code.
   ```swift
   import Foundation
   import MyDependency
   ```