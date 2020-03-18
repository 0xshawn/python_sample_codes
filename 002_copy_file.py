"""
┌──────────────────┬────────┬───────────┬───────┬────────────────┐
│     Function     │ Copies │   Copies  │Can use│   Destination  │
│                  │metadata│permissions│buffer │may be directory│
├──────────────────┼────────┼───────────┼───────┼────────────────┤
│shutil.copy       │   No   │    Yes    │   No  │      Yes       │
│shutil.copyfile   │   No   │     No    │   No  │       No       │
│shutil.copy2      │  Yes   │    Yes    │   No  │      Yes       │
│shutil.copyfileobj│   No   │     No    │  Yes  │       No       │
└──────────────────┴────────┴───────────┴───────┴────────────────┘
"""

from shutil import copyfile
copyfile(src, dst)
