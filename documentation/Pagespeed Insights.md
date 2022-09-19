# Google PageSpeed Insights
## Initialize 
```py
from googlewrapper import PageSpeed

page_speed = PageSpeed(API_KEY)
```
## Methods
## Examples
```
PSI_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

from googlewrapper import PageSpeed

page_speed = PageSpeed(PSI_KEY)

page_speed.set_url('https://www.domain.com/')
page_speed.set_device('MOBILE')

df = page_speed.pull()
```
