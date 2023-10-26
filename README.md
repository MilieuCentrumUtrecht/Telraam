# Telraam

## Omschrijving

Rapportage en analyse scripts voor het Milieucentrum Utrecht Telraam project.

## Installatie

Clone the repository.
```
git clone https://github.com/MilieuCentrumUtrecht/Telraam.git
cd Telraam
```

Create a conda environment.
```
conda env create -f environment.yml
conda activate telraam
conda develop .
```

Start a notebook server.
```
python -m ipykernel install --user --name=telraam
jupyter notebook
```
