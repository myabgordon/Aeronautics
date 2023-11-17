import matplotlib.pyplot as plt
import os

t = []
A = []
V = []
Velocity = []

save_directory = "graphs"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_graph(directory, filename):
    create_directory(directory)
    full_path = os.path.join(directory, filename)
    plt.savefig(full_path)

def read_data():
    with open("data.txt", 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            t.append(float(data[0]))
            A.append(float(data[1]))
            V.append(float(data[2]))
            Velocity.append(float(data[3]))

def graph_A():
    # Plot the data
    plt.plot(t, A, label='Amps (A)', linestyle='-')
    # Add labels and a legend
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.title('Current draw over time')
    plt.legend()
    plt.grid(True)
    save_graph(save_directory, "graph_A.png")
    plt.close('all')

def graph_V():
    # Plot the data
    plt.plot(t, V, label='Voltage (V)', linestyle='-')
    # Add labels and a legend
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('Time vs Voltage')
    plt.legend()
    plt.grid(True)
    save_graph(save_directory, "graph_V.png")
    plt.close('all')


def graph_Velo():
    # Plot the data
    plt.plot(t, Velocity, label='Velocity (m/s)',  linestyle='-')
    # Add labels and a legend
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity over time')
    plt.legend()
    plt.grid(True)
    save_graph(save_directory, "graph_Velo.png")
    plt.close('all')


def graph_ALL():
    # Plot all data series on the same graph
    plt.plot(t, A, label='Current (A)', linestyle='-')
    plt.plot(t, V, label='Voltage (V)', linestyle='-')
    plt.plot(t, Velocity, label='Velocity (m/s)', linestyle='-')
    # Add labels and a legend
    plt.xlabel('Time (s)')
    plt.ylabel('Values')
    plt.title('Flight Stats over time')
    plt.legend(["Current (A)","Voltage (V)","Velocity (m/s)"])
    plt.grid(True)
    save_graph(save_directory, "graph_ALL.png")
    plt.close('all')


def main():
    read_data() # Gather data from txt file
    # Create graph
    graph_A()
    graph_V()
    graph_Velo()
    graph_ALL()


if __name__ == "__main__":
    main()
    print("Graphs Created")
