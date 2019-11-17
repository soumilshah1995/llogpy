
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/soumilshah1995)


# llogpy 

#### what is llogpy ?
* llogpy is a open source logging modules developed for people who want to log certain methods in a class 
or a function.
* all you have to do is decorate a function with @logMethod. If you want to log entire class i mean all methods in a class 
just decorate with @logClass
* please refer to examples on how to use llogpy
* Note Logging methods dosent works  on static function in class 


<img width="542" alt="Screen Shot 2019-11-06 at 8 35 47 AM" src="https://user-images.githubusercontent.com/39345855/68302653-6fc8f700-0070-11ea-8d3b-1f1213f4579d.png">




## Installation

```bash
pip install llogpy
```
## Usage


```python
from llogpy.llogpy import logMethod,logClass


class A(object):
    def __init__(self):
        pass

    @logMethod
    def method(self):
        print(" I am a method ")

    @logMethod
    def clsmethod(cls):
        print(" i am a class method ")


if __name__ == "__main__":
    obj = A()
    obj.method()
    obj.clsmethod()


```

### Example 2

```python
from llogpy.llogpy import logMethod,logClass

@logClass
class A(object):
    def __init__(self):
        pass

    def method(self):
        print(" I am a method ")


    def clsmethod(cls):
        print(" i am a class method ")


if __name__ == "__main__":
    obj = A()
    obj.method()
    obj.clsmethod()


```



## Authors

## Soumil Nitin Shah 
Bachelor in Electronic Engineering |
Masters in Electrical Engineering | 
Master in Computer Engineering |

* Website : https://soumilshah.herokuapp.com
* Github: https://github.com/soumilshah1995
* Linkedin: https://www.linkedin.com/in/shah-soumil/
* Blog: https://soumilshah1995.blogspot.com/
* Youtube : https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw?view_as=subscriber
* Facebook Page : https://www.facebook.com/soumilshah1995/
* Email : shahsoumil519@gmail.com



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


