import matplotlib.pyplot as plt
import tempfile

def create_flowchart():

    plt.figure()

    steps = ["Start", "Collect", "Process", "Analyze", "Result"]

    x = range(len(steps))
    y = [1]*len(steps)

    plt.plot(x, y, marker="o")

    for i, step in enumerate(steps):
        plt.text(i, 1.02, step, ha="center")

    plt.axis("off")

    file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(file.name)

    return file.name


def create_bar_chart():

    plt.figure()

    labels = ["A", "B", "C", "D"]
    values = [10, 20, 15, 30]

    plt.bar(labels, values)

    file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(file.name)

    return file.name
