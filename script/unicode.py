import os
import re

def parse_unicode_code(token):
    """解析各種格式的 Unicode 碼位，回傳整數或 None"""
    token = token.strip().upper()
    if not token:
        return None
    
    # 移除 U+ 或 U 前綴
    if token.startswith('U+'):
        token = token[2:]
    elif token.startswith('U'):
        token = token[1:]
    elif token.startswith('0X'):
        token = token[2:]
    
    # 嘗試轉換十六進位
    try:
        return int(token, 16)
    except ValueError:
        return None

def expand_unicode_ranges(parts):
    """解析並展開 Unicode 範圍表達式，回傳字元列表"""
    characters = []
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # 先找範圍分隔符（~ 或 -）
        separator = None
        if '~' in part:
            separator = '~'
        elif '-' in part:
            separator = '-'
        
        if separator:
            # 處理連續範圍
            start_str, end_str = part.split(separator, 1)
            start = parse_unicode_code(start_str)
            end = parse_unicode_code(end_str)
            
            if start is not None and end is not None:
                if start > end:
                    start, end = end, start  # 自動交換
                for code in range(start, end + 1):
                    try:
                        characters.append(chr(code))
                    except (ValueError, OverflowError):
                        pass
        else:
            # 處理單獨字符
            code = parse_unicode_code(part)
            if code is not None:
                try:
                    characters.append(chr(code))
                except (ValueError, OverflowError):
                    pass
    
    return characters

def generate_filename(ranges_input):
    """根據輸入範圍產生檔案名稱"""
    # 移除多餘空格
    clean_input = ranges_input.replace(' ', '')
    # 限制檔名長度（避免太長）
    if len(clean_input) > 50:
        clean_input = clean_input[:50]
    # 替換不適合檔名的字元
    clean_input = re.sub(r'[\\/*?:"<>|]', '_', clean_input)
    return f"unicode_{clean_input}.txt"

def save_to_file(characters, filename):
    """將字元列表儲存到檔案"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(''.join(characters))
        print(f"已儲存至檔案：{filename}")
        print(f"共輸出 {len(characters)} 個字元")
        return True
    except Exception as e:
        print(f"儲存檔案失敗：{e}")
        return False

def main():
    print("=" * 50)
    print("Unicode 字元輸出工具")
    print("支援16進制：U1B001, U+1B001, 0x1B001, 1B001")
    print("格式示例：1B001,1B003~1B005,U+4E00")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 50)
        user_input = input("請輸入 Unicode 範圍（或輸入 q 離開）：").strip()
        
        if user_input.lower() in ('q', 'quit', 'exit'):
            print("感謝使用，再見！")
            break
        
        if not user_input:
            print("請輸入有效的範圍")
            continue
        
        # 先保留原始輸入用於檔名
        original_input = user_input
        
        # 支援逗號分隔多個範圍
        if ',' in user_input:
            parts = user_input.split(',')
        else:
            parts = [user_input]
        
        # 展開並取得字元
        characters = expand_unicode_ranges(parts)
        
        if not characters:
            print("沒有有效的 Unicode 碼位，請重新輸入")
            print("範例：1B001~1B005 或 U+4E00,U+4E01 或 4E00-4E10")
            continue
        
        # 輸出到螢幕（連續顯示）
        print(f"\n輸出結果（共 {len(characters)} 個字元）：")
        output_str = ''.join(characters)
        # 如果太長就只顯示前100個字元
        if len(output_str) > 100:
            print(output_str[:100] + "...(省略)")
        else:
            print(output_str)
        
        # 儲存到檔案
        filename = generate_filename(original_input)
        save_to_file(characters, filename)

if __name__ == "__main__":
    main()