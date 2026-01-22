# Key and Value Weights Are Probably All You Need
### On the Necessity of the Query, Key, Value Weight Triplet in Decoder-Only Transformers

Official implementation and model weights for the paper: **"Key and Value Weights Are Probably All You Need"** ([arXiv:2510.23912](https://arxiv.org/abs/2510.23912)).

This repository investigates the redundancy of the standard $W_Q$, $W_K$, and $W_V$ weight triplet in transformer architectures. We demonstrate that decoder-only models can maintain performance while significantly reducing parameter counts by modifying or eliminating the explicit Query weight matrix.

---

## 🚀 Quick Start

### 1. Model Checkpoints
Pre-trained checkpoints at various training stages (50k, 100k, and 104k steps) are available for download:
* **[Download from Google Drive](https://drive.google.com/drive/folders/1jpo04DxXl-VZ3llkxWox78hS8ML-1FOy?usp=sharing)**

### 2. Data Preparation
We utilize the **OpenWebText** dataset. Follow these steps to prepare the environment:
1. **Dataset Acquisition:** Run `Data_Handling.ipynb` to download and preprocess the raw data.
2. **Reproducibility:** Run `Generate_Indices.ipynb` to ensure consistent data shuffling and splitting.
3. **Configuration:** Generate the necessary training configurations by running `/configs/configurator_creator.ipynb`.

### 3. Training
To initiate training on a specific GPU (e.g., GPU 0), use the following command:

python train.py configs/configs_untied/config_untiedw_original.py --gpu 0

---

## 🛠 Architecture

The codebase is built upon [nanoGPT](https://github.com/karpathy/nanoGPT) by Andrej Karpathy. The attention mechanism has been modified to support experiments involving tied weights and reduced-parameter projections as described in the paper.

---

## 📝 Citation

If you find this work useful in your research, please cite:

```bibtex
@article{karbevski2025key,
  title={Key and Value Weights Are Probably All You Need: On the Necessity of the Query, Key, Value weight Triplet in Decoder-Only Transformers},
  author={Karbevski, Marko and Mijoski, Antonij},
  journal={arXiv preprint arXiv:2510.23912},
  year={2025}
}
```

---

## 🙏 Acknowledgments

We extend our gratitude to Andrej Karpathy for the nanoGPT repository, which served as the foundational framework for our experiments.
