# qoverview

A vertical space extended QTreeView.

The last row in default QTreeView always stays on bottom, this little project extends the vertical space so the view can be scrolled until last row hit the top of view. Which behaves like modern text editor that has virtual space enabled after last line.

![qoverview](https://user-images.githubusercontent.com/3357009/100614638-641e3180-3351-11eb-8c45-12cbc9c1c1d5.gif)


### Run Example
[Qt5.py](https://github.com/mottosso/Qt5.py) is required.
Or modify the scripts to use your Python Qt binding.

```shell script
cd qoverview
python -m example
```

### Usage

```python
# your widget
class MyView(QtWidgets.QTreeView):
...
```
:point_down:
```python
# your widget, but superclass replaced
class MyView(qoverview.VerticalExtendedTreeView):
...
```

### How it works
See `paintEvent` and you should get the picture. :relaxed:

### Limitation
* Scroll mode must be `ScrollPerPixel`.
* Size adjust policy must be `AdjustIgnored`.
* Row height must be uniformed.
* ~~Scroll bar may flicker during window resizing.~~


### TODO

Currently only QTreeView extended, would be great to extend all QAbstractItemView subclasses. If it's possible.
