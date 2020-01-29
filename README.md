He trabajado con **Miniconda** en su versión 3 (versión pequeña y minimalista de Anaconda, una distribución que incluye Python y otros paquetes para data science y computación científica)

**Miniconda** incluye Python, pip y conda (y otros paquetes necesarios para su funcionamiento).

Con el gestor de paquetes y entornos, **conda**, he creado un entorno para este trabajo:
```bash
$ conda create env_name python=3.6.10
```
Es necesario activar el entorno:
```bash
$ conda activate env_name
```
Instalar librerías necesarias:
```bash
# En mi caso, utilicé JupyterLab
(env_name) $ conda install -c conda-forge jupyterlab pandas
```
Abrir JupyterLab:
```bash
(env_name) $ jupyter lab
```

###  **Hands on!**