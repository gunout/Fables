import time
import os

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_frame(frame):
    clear_terminal()
    print(frame)
    time.sleep(1)  # Changez le temps de pause pour un effet plus rapide

def animate_dialogue(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Pause pour chaque caractère
    print()  # Pour sauter à la ligne suivante
    time.sleep(1)  # Pause avant le prochain dialogue

def main():
    frames = [
        r"""
         (  )
        (    )
       (      )
        \    /
         \  /
          \/ 
         /\
        /  \ 
       /    \ 
      /      \
    _/        \_
    """,
        r"""
         _    
        ( \    
         \ \   
          \ \  
           \_\ 
          / /
         / /
        / /
       / /
      / /
    _/ /
    """,
        r"""
         (  )
        (    )
       (      )
        \    /
         \  /
          \/ 
         /\
        /  \ 
       /    \ 
      /      \
    _/        \_
    """,
        r"""
          .--.
        .'_\/_'.
        '. /\ .'
          "||"
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
            ||
          _||_
         |____|
    """,
        r"""
         (  )
        (    )
       (      )
        \    /
         \  /
          \/ 
         /\
        /  \ 
       /    \ 
      /      \
    _/        \_
    """,
        r"""
          _    
        .' '.    
      _/     \_  
    _/         \_ 
    """,
    ]

    dialogue = [
        "Le Corbeau prend un fromage dans son bec.",
        "Le Renard, intrigué, s'approche et dit :",
        "Bonjour, beau Corbeau, quel magnifique plumage !",
        "Si tu chantes aussi bien que tu es beau, je suis sûr que tu es le roi des oiseaux !",
        "Le Corbeau, flatté, ouvre le bec pour chanter.",
        "Le fromage tombe, et le Renard s'en empare.",
        "Moralité : Ne vous laissez pas tromper par de vaines flatteries."
    ]

    for frame in frames:
        print_frame(frame)

    for line in dialogue:
        clear_terminal()
        animate_dialogue(line)

if __name__ == "__main__":
    main()

