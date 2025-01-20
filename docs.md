# Gambling Simulator Documentation

## 1. Gameplay

### 1.1. Home Screen

### 1.2. Achievements

### 1.3. Betting & Spinning

### 1.4. Bar

### 1.5. Insurance

### 1.6. Bank

### 1.7. High Rollers Club

### 1.8. Bankruptcy

### 1.9. Endings

## 2. Mechanics

### 2.1. Upgradable Stats

### 2.2. Spinning

### 2.3. Loans

### 2.4. Insurance

### 2.5. Conditional Events

### 2.6. Endings

## 3. Mods

### 3.1. How to Use Mods

Mods are Python files placed in your `mods` folder, located in the same directory as your game file (whether executable or Python). They can add dialogue, text, scripting, events, and more to Gambling Simulator's gameplay. When mods are loaded, starting the game will prompt a message that lists your currently loaded mods.

#### 3.1.1. Disabled.txt

To disable mods without moving them from your `mods` folder, create a file called `disabled.txt` in the `mods` folder. Add the name of each mod file you wish to disable on a new line, omitting the file extension.

### 3.2. Mod Structure

Mods are Python files containing a self-titled class, and each method of the class does different things.

#### 3.2.1. Metadata Methods

`__str__(self)`: defines the mod's name as a plain string. The mod name should be the same as the file name and class name. Expects a string to be returned.

`name(self, globals)`: defines the mod's name, with optional formatting. The formatted name should be the same as in `__str__`, the file name, and class, but can contain colorama ANSI sequences. Expects a string to be returned.

`description(self, globals)`: defines the mod's description, with optional formatting. Can contain colorama ANSI sequences. Expects a string to be returned.

#### 3.2.2. Scripting Methods
