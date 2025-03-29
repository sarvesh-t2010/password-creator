# Ingenious Password Creator

## Overview
This program generates a unique password based on user input. The password is created by applying various transformations to user-provided answers, ensuring both uniqueness and security.

## Features
- **Removes spaces**: Spaces in inputs are replaced with exclamation marks.
- **Reverses words**: Some inputs are reversed to increase randomness.
- **Capitalization rules**: The first letter of some inputs is capitalized.
- **Symbol inclusion**: Adds special characters based on input length.
- **Default values**: If invalid input is given, the program assigns default values.

## How It Works
1. The user answers the following questions:
   - Birth month
   - Favorite movie
   - Favorite president
   - Favorite car
2. The program processes these inputs and applies transformations.
3. A password is generated using a combination of:
   - First two letters of the birth month (uppercase)
   - Length of the favorite movie multiplied by a predefined number
   - Reversed portions of the movie and car names
   - Special symbols based on car name length
4. The generated password is displayed to the user.

## Example Output
```
--------------------------------------
Your school password is: JFKIA8v!tor$ic
--------------------------------------
```

## How to Run
1. Ensure you have Python installed.
2. Copy and paste the script into a Python environment.
3. Run the script and follow the prompts.

## Author
**Sarvesh Thiagarajan**

Date Created: **12/3/25**

