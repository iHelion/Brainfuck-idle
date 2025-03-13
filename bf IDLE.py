import sys

def brainfuck_interpreter(code, input_stream=''):
    tape = [0] * 30000
    ptr = 0
    output = ''
    input_ptr = 0
    code_ptr = 0
    bracket_map = {}
    stack = []
    
    for i, cmd in enumerate(code):
        if cmd == '[':
            stack.append(i)
        elif cmd == ']':
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    
    while code_ptr < len(code):
        cmd = code[code_ptr]
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == ',':
            if input_ptr < len(input_stream):
                tape[ptr] = ord(input_stream[input_ptr])
                input_ptr += 1
            else:
                tape[ptr] = 0
        elif cmd == '[' and tape[ptr] == 0:
            code_ptr = bracket_map[code_ptr]
        elif cmd == ']' and tape[ptr] != 0:
            code_ptr = bracket_map[code_ptr]
        
        code_ptr += 1
    
    return output

def brainfuck_idle():
    print("\nWelcome to Brainfuck IDLE!")
    print("Type your Brainfuck code below. Type ':run' to execute, ':exit' to quit, ':clear' to clear.")
    
    code = ""
    while True:
        line = input(">>> ")
        if line == ':exit':
            print("Exiting Brainfuck IDLE...")
            break
        elif line == ':clear':
            code = ""
            print("Code cleared.")
        elif line == ':run':
            print("Output:")
            print(brainfuck_interpreter(code))
        else:
            code += line + '\n'

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        print("Output:")
        print(brainfuck_interpreter(code))
    else:
        brainfuck_idle()

if __name__ == "__main__":
    main()