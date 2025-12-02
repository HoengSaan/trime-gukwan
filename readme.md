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

- 佈局種類
  - 「**菊韻**」本身佈局爲過度複雜，試圖將過多功能塞進主鍵盤佈局之中，部份人或不能接受使用。
  - 「**菊韵**」主鍵盤同普通36鍵佈局區別不大，亦允許拼音提示出現在相應鍵位，方便雙拼・三拼學習者使用。（「韵」爲「韻」異字）
  - 「**菊韻五段**」是爲探求在少於26鍵情況，有無更好佈局，在此基礎上，毋須如同9鍵，14鍵，18鍵需要對方案拼寫進行更改。此佈局參考Google Godan日文輸入法，有針對粵拼輸入作出優化。具體請見下方說明。
- 假名輸入方式
  - 由於Rime日語輸入法不甚理想，亦非所有方案支持輸入假名，故設計假名佈局令用家可直輸假名，不倚賴任何方案。
  - 不諳日語者，假名輸入方式請無腦選擇五十音圖，使用該佈局之主題名均以「50」結尾。
  - 通曉日語者，可根據自身需求選擇使用。
    - フリック：簡潔，基於12鍵佈局更改之20鍵佈局，濁音直出，小假名直出。
    - 五十音圖：臃腫，但支持更多特殊假名輸入，如愛奴語假名、臺語假名等。
- 鍵盤高度
  - 菊韻鍵盤高度較高，佔用畫面較多，不慣可用「**小-**」或自行修改。
- 所有佈局一覽
  - **菊韻**：36+鍵煩雜佈局，無提示，高鍵盤，フリック假名輸入
  - **菊韻**50：同上，五十音圖輸入
  - 小**菊韻**：36+鍵煩雜佈局，無提示，中鍵盤，フリック假名輸入
  - 小**菊韻**50：同上，五十音圖假名輸入
  - **菊韵**：36+鍵複雜佈局，有提示，高鍵盤，フリック假名輸入
  - **菊韵**50：同上，五十音圖輸入
  - 小**菊韵**：36+鍵煩雜佈局，無提示，中鍵盤，フリック假名輸入
  - 小**菊韵**50：同上，五十音圖假名輸入
  - **菊韻五段**：17鍵五段佈局，無提示，高鍵盤，フリック假名輸入
  - **菊韻五段**50：同上，五十音圖輸入
  - 小**菊韻五段**：17鍵五段佈局，無提示，中鍵盤，フリック假名輸入
  - 小**菊韻五段**50：同上，五十音圖輸入

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
- 普雙：36鍵，自然碼｜小鶴【限菊韵】
- 九宮：9鍵，萬象九宮格｜霧凇九宮格｜菊韻九宮格（下劃直接輸入數字以輸入聲調）
  - 漢英混打須使用「英」打開36鍵鍵盤


默認只有部分方案，手動適配方式如下：

```yaml
  my_cangjie:
    import_preset: cangjie5
```

### 配色佈局

此處僅簡單展示效果同基本用法，實際佈局由於版本更新或有分別，其他鍵盤佈局同配色方案請自行探索。

上方符號可長壓或上劃，上方功能只能長壓；下方符號同功能通常爲左右劃，或者下劃。

| ![](/pic/1.jpg)                                              | ![](/pic/2.jpg)                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 主鍵盤（星天｜黑白深色｜原作者配色）【菊韻】                 | 主鍵盤（白夜｜黑白淺色｜原作者配色）【菊韵】拼音提示         |
| ![](/pic/3.jpg)                                              | ![](/pic/4.jpg)                                              |
| 平假名フリック鍵盤（酒紅｜紅色深色）                         | 片假名フリック鍵盤（峯櫻｜紅色淺色）                         |
| ![](/pic/5.jpg)                                              | ![](/pic/6.jpg)                                              |
| 平假名五十音圖鍵盤（番瓜｜黃色深色）；舊假名無法顯示<br />下劃同左劃爲濁音，右劃爲半濁音，上劃爲捨假名（細字） | 片假名五十音圖鍵盤（金盞菊｜黃色深色）；舊假名無法顯示<br />下劃同左劃爲濁音，右劃爲半濁音，上劃爲捨假名（細字） |
| ![](/pic/7.jpg)                                              | ![](/pic/8.jpg)                                              |
| 希臘文鍵盤（松葉｜綠色深色）                                 | 西里爾文鍵盤（竹林｜綠色淺色）                               |
| ![](/pic/9.jpg)                                              | ![](/pic/10.jpg)                                             |
| 萬國音標鍵盤（矢車菊｜藍色深色）；部份音標無法正常顯示       | 諺文鍵盤（紫陽｜藍色淺色）<br />韻尾須下劃或左劃輸入，其他同普通諺文輸入法無異 |
| ![](/pic/11.jpg)                                             | ![](/pic/12.jpg)                                             |
| 編輯鍵盤（薰衣草｜紫色深色）；選擇無法正常工作               | 數字鍵盤（紫藤｜紫色深色）                                   |
| ![](/pic/13.jpg)                                             | ![](/pic/14.jpg)                                             |
| 倉頡鍵盤（菊韻｜其他）                                       | 注音鍵盤（冶遊｜其他）                                       |
| ![](/pic/15.jpg)                                             | ![](/pic/16.jpg)                                             |
| 九宮格鍵盤（椰海｜其他）<br />「36」即36鍵鍵盤，以解決九宮格無法漢英混打問題；下劃輸入數字 | 新基本符號（白炭｜其他）；配合九宮格鍵盤、菊韻五段使用       |
| ![](/pic/17.jpg)                                             |                                                              |
| 主鍵盤（海傍｜其他）【菊韻五段】                             |                                                              |

菊韻五段是爲探求在少於26鍵情況，有無更好佈局，在此基礎上，毋須如同9鍵，14鍵，18鍵需要對方案拼寫進行更改。此佈局參考Google Godan日文輸入法，有針對粵拼輸入作出優化。此輸入法同九宮格鍵盤有所不同，並不影響出詞，細字（如「A」有「R」，「S」有「SH」）劃向任一方向即可是輸入，標點則只可左右劃（如「N」個感歎號要左劃，問號要右劃）。爲保證同其他拼音之相容性 ，粵式五段可輸入26個字母，亦留有36鍵鍵盤備用。

由於粵語有濁音方言少，故取消細字輸入。

（此部份僅限粵語）下爲拼音修改建議，菊韻三拼同理：

- <mark>建議使用[J++（擴展粵拼）](https://docs.google.com/spreadsheets/d/19puWUoeYGflSuJj7mNm7maTX5bA2tkjNDESaMTBwPaw/edit?usp=sharing)</mark>
- 輔音
  - 如心母爲「sl /ɬ/」「th /θ/」等建議將拼音改爲「s」，審母則從「s」改爲「sh」
  - 翹舌建議使用「zh・ch・sh」，而非「zj・cj・sj」等。
  - 日母「nj /ȵ/」建議簡拼爲「r」。
  - 脣化「gw /kʷ/・kw /kʰʷ/」、脣齒化「gv /kᶹ/・kv /kʰᶹ/」）聲母建議簡拼爲「x」「q」（可調轉）。
- 單元音
  - 「oe・io」「ae」「ia・iaa」等元音建議簡拼爲「e」
  - 「aa」等元音可簡拼爲「r」
  - 「eo /ɵ/・ea /ə/」等元音建議簡拼爲「u」（根據情況亦可簡拼爲「a」）
- 複元音
  - 「ooi・ooy」等元音建議簡拼爲「ui・uy」
  - 「ook・oong」等元音建議簡拼爲「ok・ong」

## 使用

安裝直接丟入`/rime`文件夾，然之後選擇主題即可。

### 注意事項

- 不建議使用按鍵氣泡，顯示效果有問題。
- 並無對橫屏介面做任何適配。
- 菊韻主題各個版本並無互相依賴，選擇合適自身版本即可刪除其他版本。