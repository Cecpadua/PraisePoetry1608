# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from pypinyin import pinyin, Style

def get_pinyin_initials(text):
    # 将中文字符串转换为拼音列表，Style.FIRST_LETTER 表示获取首字母
    pinyin_list = pinyin(text, style=Style.FIRST_LETTER)
    
    # 将拼音列表转换为字符串
    initials = ''.join([item[0] for item in pinyin_list])
    
    return initials

print(get_pinyin_initials("""
                          
    26_主先爱我
1、主在天上何等荣耀，世上君王全不如。
至高至尊上帝同等，救主焉能怜爱我。
我在世间极其卑贱，力量德行也全无。
谁知非我先爱恩主，乃是耶稣先爱我。

2、颂赞救主爱极广厚，垂怜世人为罪奴。
舍弃尊荣欢欣临世，实因耶稣先爱我。
卧槽卑微居野饥饿，祷于山上行于湖。
多行奇事屡经苦楚，皆显耶稣先爱我。

3、主被钉于十字苦架，为我罪人担罪辜。
此事希奇惊动天地，证明耶稣先爱我。
等不多时得见恩主，我蒙拯救常欢呼。
何等慈怜出奇恩惠，赞美耶稣先爱我。                    
       
""").strip().replace(" ", "").replace("\n", " "))