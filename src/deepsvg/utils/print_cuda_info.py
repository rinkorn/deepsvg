import torch


def print_cuda_info():
    print(f"torch version: {torch.__version__}")
    print(f"N devices: {torch.cuda.device_count()}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    print("CUDA version:", torch.version.cuda)
    print(f"CuDNN available: {torch.backends.cudnn.m.is_available()}")
    cudnn = torch.backends.cudnn.version()
    cudnn_major = cudnn // 1000
    cudnn_minor = cudnn % 1000 // 100
    cudnn_patch = cudnn % 1000 % 100
    print("cuDNN version:", ".".join([str(cudnn_major), str(cudnn_minor), str(cudnn_patch)]))
    print(f"Devices[0] name: {torch.cuda.get_device_name(0)}")


if __name__ == "__main__":
    print_cuda_info()
