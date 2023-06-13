import operator
import pandas as pd

class Instance:
    def __init__(self, Name, API_Name, GPUs, GPU_model, GPU_memory, Monthly_cost, CUDA_Compute_Capability):
        self.Name = Name
        self.API_Name = API_Name
        self.GPUs = GPUs
        self.GPU_model = GPU_model
        self.GPU_memory = GPU_memory
        self.Monthly_cost = Monthly_cost
        self.CUDA_Compute_Capability = CUDA_Compute_Capability*GPUs

def read_instances_from_excel(file_path):
    df = pd.read_excel(file_path)
    instances = []
    for index, row in df.iterrows():
        instances.append(Instance(row['Name'], row['API Name'], row['GPUs'], row['GPU model'], row['GPU memory'], row['Monthly cost in shekels'], row['CUDA Compute Capability']))
    return instances

def get_instances_within_budget(budget, instances):
    instances = sorted(instances, key=operator.attrgetter('CUDA_Compute_Capability'), reverse=True)

    selected_instances = []
    total_gpus = 0
    gpu_types = {}

    for instance in instances:
        while budget - instance.Monthly_cost >= 0:
            budget -= instance.Monthly_cost
            selected_instances.append(instance)
            total_gpus += instance.GPUs
            if instance.GPU_model in gpu_types:
                gpu_types[instance.GPU_model] += instance.GPUs
            else:
                gpu_types[instance.GPU_model] = instance.GPUs

    gpu_report = ', '.join([f"{value}x {key}" for key, value in gpu_types.items()])

    return selected_instances, total_gpus, gpu_report


# Read instances from Excel file
fn = "Amazon EC2 Instance Comparison.xlsx"
instances = read_instances_from_excel(fn)  # Replace with your file path

# Set your budget here
budget = 100000

selected_instances, total_gpus, gpu_report = get_instances_within_budget(budget, instances)

print(f"Selected {len(selected_instances)} instances with total of {total_gpus} GPUs.")
print(f"GPUs: {gpu_report}")
