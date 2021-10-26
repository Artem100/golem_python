import sys
from golem import main


def run():
    path = sys.argv[-1]
    file = path.split("\\tests\\")[1]
    del sys.argv[-1]
    sys.argv.append("run")
    proj = "automation_practice"
    sys.argv.append(proj)
    sys.argv.append(file)
    sys.argv.append("-e")
    env = 'QA'
    for i in env.split(" "):
        sys.argv.append(i)
    main.execute_from_command_line(".")


if __name__ == '__main__':
    run()

