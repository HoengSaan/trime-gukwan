# 菊韻同文主題

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

本作品採用[創意共享 署名-非商業性-相同方式共享 4.0 國際版許可證](cc-by-nc-sa)。

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

**此爲本人自用同文輸入法（Trime）專用主題。基於[Wenti-D/Astralwelkin](https://github.com/Wenti-D/Astralwelkin)，源文件以[MIT 許可](https://mit-license.org/)發佈。**

### 其他菊韻項目

- 菊韻粵語：[rime-gukwan: 菊韻粵語輸入方案 基於中州韻 Cantonese IME (RIME Scheme)](https://github.com/HoengSaan/rime-gukwan)
- 菊韻和語：[rime-kikwin: 菊韻日本語入力法 基於中州韻 Japanese IME (RIME Scheme)](https://github.com/HoengSaan/rime-kikwin)

## 介紹

菊韻使用36+鍵佈局（QWERTY字母鍵26個＋一行數字鍵10個），配色多樣，自帶多種鍵盤，適配多種佈局。

### 版本說明

- 佈局複雜度同拼音提示
  - 「**菊韻**」本身佈局爲過度複雜，試圖將過多功能塞進主鍵盤佈局之中，部份人或不能接受使用。
  - 「**菊韵**」主鍵盤同普通36鍵佈局區別不大，亦允許拼音提示出現在相應鍵位，方便雙拼・三拼學習者使用。（「韵」爲「韻」異字）
- 假名輸入方式
  - 由於Rime日語輸入法不甚理想，亦非所有方案支持輸入假名，故設計假名佈局令用家可直輸假名，不倚賴任何方案。
  - 不諳日語者，假名輸入方式請無腦選擇五十音圖，使用該佈局之主題名均以「50」結尾。
  - 通曉日語者，可根據自身需求選擇使用。
    - フリック：簡潔，基於12鍵佈局更改之20鍵佈局，濁音直出，小假名直出。
    - 五十音圖：臃腫，但支持更多特殊假名輸入，如愛奴語假名、臺語假名等。
- 鍵盤高度
  - 菊韻鍵盤高度較高，佔用畫面較多，不慣可用「**小-**」或自行修改。
- 所有佈局一覽
  - 菊韻：36+鍵煩雜佈局，無提示，高鍵盤，フリック假名輸入
  - 菊韻50：同上，五十音圖輸入
  - 小菊韻：36+鍵煩雜佈局，無提示，中鍵盤，フリック假名輸入
  - 小菊韻50：同上，五十音圖假名輸入
  - 菊韵：36+鍵複雜佈局，有提示，高鍵盤，フリック假名輸入
  - 菊韵50：同上，五十音圖輸入
  - 小菊韵：36+鍵煩雜佈局，無提示，中鍵盤，フリック假名輸入
  - 小菊韵50：同上，五十音圖假名輸入

### 字體

- WD-XL Lubrifont / WD-XL 滑油字：僅用於按鍵，來源爲[NightFurySL2001/WD-XL-font](NightFurySL2001/WD-XL-font)。由於**滑油字**闕失部份字符，<mark>部分佈局有闕字現象</mark>，不能接受者可使用其他字型。
- Shanggu / 尚古：僅用於候選欄，來源爲[GuiWonder/Shanggu](https://github.com/GuiWonder/Shanggu)。由於**尚古**闕失部分罕有字，不能接受者可使用**字雲**、**天珩字庫**或其他字型。（亦可作爲後備字型設置）
- Chocolate Classical Sans / 朱古力黑體：除按鍵・按鍵註釋・候選欄之外，來源爲[MoonlitOwen/ChocolateSans](https://github.com/MoonlitOwen/ChocolateSans)。

以上文件皆隨源文件以[SIL Open Font License 1.1](https://openfontlicense.org/)發佈。

### 適配佈局

- 粵拼：36鍵，適配[菊韻粵語](https://github.com/HoengSaan/rime-gukwan)，有反查快捷開關，**菊韵版有三拼提示**
- 粵雙：37鍵，**菊韵版有雙拼提示**
- 倉頡：36鍵，適配[五代倉頡](https://github.com/rime/rime-cangjie)｜[六代倉頡](https://github.com/LEOYoon-Tsaw/Cangjie6)｜[速成]([rime/rime-quick: [速成]輸入方案](https://github.com/rime/rime-quick))｜[微軟速成](https://github.com/philipposkhos/rime-ms-quick)
- 注音：40鍵，適配[大千式注音](https://github.com/rime/rime-bopomofo)
- 行列：40鍵，適配[行列30](https://github.com/rime/rime-array/blob/master/array30.schema.yaml)
- 普雙：36鍵，自然碼｜小鶴【限菊韵，須手動進行適配】

適配方式如下：

```yaml
  my_cangjie:
    import_preset: cangjie5
```

### 配色佈局

| ![](/pic/1.jpg)                              | ![](/pic/2.jpg)                                      |
| -------------------------------------------- | ---------------------------------------------------- |
| 主鍵盤（星天｜黑白深色｜原作者配色）【菊韻】 | 主鍵盤（白夜｜黑白淺色｜原作者配色）【菊韵】拼音提示 |
| ![](/pic/3.jpg)                              | ![](/pic/4.jpg)                                      |
| 平假名フリック鍵盤（酒紅｜紅色深色）         | 片假名フリック鍵盤（峯櫻｜紅色淺色）                 |
| ![](/pic/5.jpg)                              | ![](/pic/6.jpg)                                      |
| 平假名五十音圖鍵盤（番瓜｜黃色深色）         | 片假名五十音圖鍵盤（金盞菊｜黃色深色）               |
| ![](/pic/7.jpg)                              | ![](/pic/8.jpg)                                      |
| 希臘文鍵盤（松葉｜綠色深色）                 | 西里爾文鍵盤（竹林｜綠色淺色）                       |
| ![](/pic/9.jpg)                              | ![](/pic/10.jpg)                                     |
| 萬國音標鍵盤（矢車菊｜藍色深色）             | 諺文鍵盤（紫陽｜藍色淺色）                           |
| ![](/pic/11.jpg)                             | ![](/pic/12.jpg)                                     |
| 編輯鍵盤（薰衣草｜紫色深色）                 | 數字鍵盤（紫藤｜紫色深色）                           |
| ![](/pic/13.jpg)                             | ![](/pic/14.jpg)                                     |
| 倉頡鍵盤（菊韻｜其他色）                     | 特殊鍵盤（冶遊｜其他色）                             |

其他鍵盤佈局同配色方案請自行探索。

## 使用

安裝直接丟入`/rime`文件夾，然之後選擇主題即可。

### 注意事項

- 不建議使用按鍵氣泡，顯示效果有問題。
- 並無對橫屏介面做任何適配。
- 菊韻主題各個版本並無互相依賴，選擇合適自身版本即可刪除其他版本。