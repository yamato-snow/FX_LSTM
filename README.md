# Python環境設定と実行方法

このドキュメントでは、Pythonの環境設定と実行方法について説明します。

## 目次

1. [pyenvでのPythonバージョンの指定](#pyenvでのPythonバージョンの指定)
2. [Python仮想環境の作成とアクティベーション](#Python仮想環境の作成とアクティベーション)
3. [pipのアップデート](#pipのアップデート)
4. [仮想環境の停止](#仮想環境の停止)
5. [Pythonスクリプトをexeファイルに変換](#Pythonスクリプトをexeファイルに変換)
6. [JupyterNotebookの実行環境を構築](#JupyterNotebookの実行環境を構築)
7. [VSCodeでmdファイルをプレビュー](#VSCodeでmdファイルをプレビュー)

## pyenvでのPythonバージョンの指定

指定したいPythonのバージョン（例：3.11.5）をpyenvを使用して指定します。

```bash
pyenv local 3.11.5
```

**注：** pyenvに指定したバージョンがない場合は、以下のコマンドでインストールします。

```bash
pyenv install 3.11.5
```

## Python仮想環境の作成とアクティベーション

Pythonの仮想環境を作成します。

```bash
python -m venv .venv
```

### Windowsでのアクティベーション
- パワーシェルの場合
```bash
.venv/Scripts/activate.ps1
```

- コマンドプロンプトの場合
```bash
.venv\Scripts\activate.bat
```

### macOSでのアクティベーション

- 管理者権限の場合
```bash
source .venv/bin/activate
```

- 通常の場合
```bash
. .venv/bin/activate
```

## pipのアップデート

仮想環境内のpipをアップデートします。

```bash
python -m pip install --upgrade pip
```

## 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

## 仮想環境の停止

仮想環境を停止します。

```bash
deactivate
```

## Pythonスクリプトをexeファイルに変換

Pythonスクリプトをexeファイルに変換する方法について説明します。

### ステップ1: PyInstallerのインストール

```bash
pip install pyinstaller
```

### ステップ2: exeファイルの生成

以下のコマンドを実行してexeファイルを生成します。

- ウィンドウを表示する場合：
```bash
pyinstaller --onefile your_script.py
```

- コンソールを非表示にする場合：
```bash
pyinstaller --onefile --noconsole your_script.py
```

## JupyterNotebookの実行環境を構築

JupyterNotebookの実行環境を構築する方法について説明します。

### ステップ1: JupyterNotebookのインストール

- パワーシェルの場合
```bash
python -m pip install notebook
```

- コマンドプロンプトの場合
```bash
pip install notebook
```

### ステップ2: jupyter notebookを実行

以下のコマンドを実行してjupyter notebookを起動します。
- 通常
```bash
jupyter notebook
```

以下のコマンドを実行してjupyter notebookを起動します。
- セキュリティエラーが出た場合
```bash
python -m jupyter notebook
```

## VSCodeでmdファイルをプレビュー

Visual Studio Code（VSCode）で.md（Markdown）ファイルをプレビューするためのショートカットキーについて説明します。

### Windowsバージョン

以下のショートカットキーを使用して.mdファイルをプレビューします。

```bash
Ctrl + Shift + V
```

### MacOSバージョン

以下のショートカットキーを使用して.mdファイルをプレビューします。

```bash
Cmd + Shift + V
```