'''import black
import subprocess

def detect_language(code):
    """Detect programming language based on keywords."""
    if "def " in code or "import " in code:
        return "Python"
    elif "#include" in code or "int main()" in code:
        return "C++"
    elif "public class" in code or "System.out.println" in code:
        return "Java"
    else:
        return "Unknown"

def format_python(code):
    return black.fix_code(code)

def format_cpp(code):
    formatted_code = subprocess.run(["clang-format"], input=code.encode(), capture_output=True)
    return formatted_code.stdout.decode()

def format_java(code):
    formatted_code = subprocess.run(["google-java-format"], input=code.encode(), capture_output=True)
    return formatted_code.stdout.decode()

def pretty_print(code):
    lang = detect_language(code)
    
    if lang == "Python":
        return format_python(code)
    elif lang == "C++":
        return format_cpp(code)
    elif lang == "Java":
        return format_java(code)
    else:
        return "Unsupported language"

# User Input
user_code = input("Enter your code:\n")
formatted_code = pretty_print(user_code)
print("\nFormatted Code:\n", formatted_code)
'''
#======================================================================
#======================================================================

'''import autopep8
import black
import jsbeautifier
import sqlparse
import subprocess

def format_code(code, lang):
    if lang.lower() == "python":
        # Use 'black' for best formatting
        formatted_code = black.format_str(code, mode=black.FileMode())
        return formatted_code

    elif lang.lower() == "javascript":
        # Use jsbeautifier for JS
        return jsbeautifier.beautify(code)

    elif lang.lower() == "sql":
        # Use sqlparse for SQL
        return sqlparse.format(code, reindent=True, keyword_case="upper")

    elif lang.lower() in ["c", "cpp", "java"]:
        # Use clang-format for C, C++, Java
        try:
            process = subprocess.run(
                ["clang-format"],
                input=code.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return process.stdout.decode()
        except FileNotFoundError:
            return "Error: clang-format not installed. Install it first."

    else:
        return "Error: Language not supported."
    

user_code = input("Enter your code:\n")
formatted_code = format_code (user_code,language)
print("\nFormatted Code:\n", formatted_code) '''
#======================================================================
#======================================================================
'''import autopep8
import black
import jsbeautifier
import sqlparse
import subprocess

def format_code(code, lang):
    if lang.lower() == "python":
        formatted_code = black.format_str(code, mode=black.FileMode())
        return formatted_code

    elif lang.lower() == "javascript":
        return jsbeautifier.beautify(code)

    elif lang.lower() == "sql":
        return sqlparse.format(code, reindent=True, keyword_case="upper")

    elif lang.lower() in ["c", "cpp", "java"]:
        try:
            process = subprocess.run(
                ["clang-format"],
                input=code.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return process.stdout.decode()
        except FileNotFoundError:
            return "Error: clang-format not installed. Install it first."

    else:
        return "Error: Language not supported."

# ✅ User Input for Code and Language
user_code = input("Enter your code:\n")
language = input("Enter the language (Python, JavaScript, C, C++, Java, SQL): ").strip().lower()

formatted_code = format_code(user_code, language)
print("\nFormatted Code:\n", formatted_code)'''
#======================================================================
#======================================================================
'''import autopep8
import black
import jsbeautifier
import sqlparse
import subprocess

def format_code(code, lang):
    try:
        if lang.lower() == "python":
            formatted_code = black.format_str(code, mode=black.FileMode())
            return formatted_code
        elif lang.lower() == "javascript":
            return jsbeautifier.beautify(code)
        elif lang.lower() == "sql":
            return sqlparse.format(code, reindent=True, keyword_case="upper")
        elif lang.lower() in ["c", "cpp", "java"]:
            try:
                process = subprocess.run(
                    ["clang-format"],
                    input=code.encode(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                return process.stdout.decode()
            except FileNotFoundError:
                return "Error: clang-format not installed. Install it first."
        else:
            return "Error: Language not supported."
    except black.parsing.InvalidInput:
        return "Error: Invalid Python code. Please check syntax."

# ✅ User Input for Code and Language
user_code = input("Enter your code:\n")
language = input("Enter the language (Python, JavaScript, C, C++, Java, SQL): ").strip().lower()

formatted_code = format_code(user_code, language)
print("\nFormatted Code:\n", formatted_code)'''
#======================================================================
#======================================================================
