# Introduce  
Hi! Thanks for comming my site.  
When you want to delete duplicate sentence from your sentence, Please use duplidele.  

# Introduce  
Hi! Thanks for comming my site.  
When you want to delete duplicate sentence from your sentence, Please use duplidele.  

# How to install  
pip install duplidele  

# How to coding  

1)Delete one character at a time  

import duplidele as dd  
dd.exduplidelechar("test sentence test sentence duplicate delete", 5)  

export ⇒test sentence duplicate delete  
<img src="attach:4.JPG">![4](https://user-images.githubusercontent.com/20910951/130357300-9a72e4af-0531-4148-b6b8-2f7e0da0f733.JPG)


2)Delete word by word  

*◆最低6word以上のため発動（変更可能）*  
import duplidele as dd  
dd.exduplidele("おはよう。元気ですか？おはよう。元気ですか？猫さん。私は元気です。", 6)  

export ⇒ おはよう。元気ですか？猫さん。私は元気です。  
<img src="attach:3.JPG">![3](https://user-images.githubusercontent.com/20910951/130357295-336be47c-8de5-4864-90a8-9180d8ecbc91.JPG)

*◆最低7word以上の設定にしてしまうと発動しない*  
import duplidele as dd  
dd.exduplidele("おはよう。元気ですか？おはよう。元気ですか？猫さん。私は元気です。", 7)  

export ⇒ おはよう。元気ですか？おはよう。元気ですか？猫さん。私は元気です。  

*◆重複文章の間に他の文字が入ると発動しない*  
import duplidele as dd  
dd.exduplidele("おはよう。元気ですか？うん、おはよう。元気ですか？猫さん。私は元気です。", 6)  

export ⇒ おはよう。元気ですか？おはよう。元気ですか？猫さん。私は元気です。  

# License  
MIT  




