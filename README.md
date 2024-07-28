# Minecraft Enchantment Generator

## Description
This project is a Python script that generates a Minecraft `/give` command with enchantments. It allows users to select an item, target, and enchantments, and then generates a command that can be used in Minecraft to give the item with the specified enchantments to the target.

## Dependencies
- Python 3

## Installation

1. Clone the repository

    ```bash
    git clone https://github.com/DualsFWShield/Minecraft-give-command-generator.git
    ```

2. Install Python 3

    If you haven't already, install Python 3.x from the official website: [Python Downloads](https://www.python.org/downloads/)

3. Run the script

    ```bash
    python give-command-gen.py
    ```

## Usage

1. Run the script

    ```bash
    python give-command-gen.py
    ```

2. Select the target

    Select the target (e.g. `@s` for the player themselves)

3. Select the item

    Select the item (e.g. `acacia_button`)

4. Select the enchantments and their levels

    Select the enchantments and their levels (e.g. `Blast Protection: 3`)

5. Click the "Generate Command" button

    Click the "Generate Command" button to generate the command

6. Copy the generated command

    Copy the generated command and use it in Minecraft

## Example Output

```
/give @s acacia_button[enchantments={levels:{blast_protection:3}}] 5
```

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing
Contributions are welcome! If you'd like to add new features or fix bugs, please submit a pull request.

## Author
DualsFWShield
