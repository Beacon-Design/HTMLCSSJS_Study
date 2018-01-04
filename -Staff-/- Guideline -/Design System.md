# Design System Part 1

> Don't confuse a design system work with a rebrand or a text-dec overhaul. 
>
> The design system's patterns should be familiar not new.
>
> The job is not to invent but to curate.

### 1. Design System

1. Foundations and Principles

   > Guiding design principles, accessibility targets, animations, scaling, and grids.


2. Brand Identity

   > Fonts, colors, meaning, visual language, and white label logo/marketing related

3. Editorial Guidelines

   > Voice and tone, word list, capitalizztion, and punctuation.

4. Pattern Library

   > UI Components, page templates, and reference files [.psd, .ai, .sketch]

5. Code

   > Coding standards, supported browsers and devices, versioning, and pattern implementation



### 2. A design system will provide value if your products...

- Need to look and behave similarly
- Implement similar UI components
- Duplicate low-level functionality
- Must be white labeled or themed
- Are built on different tech stacks
- Suffer from visual regression bugs



### 3. Benefits of a design system

- Provide a single source of truth for building UIs
- Save time and money
- Increase consistency
- Decrease maintenance
- UX teams focus on the experience and dev teams on implementation
- Improve user experience through well-defined and learned behaviors.



### 4. Component Prioritization Workshop

Identifying components ( Component Prioritization Worksheet ).

### 5. Cutting up components

##### Before the Workshop

- Invite anyone with non-negligible time on the project
- Create categorized sections based on the component checklist
- Print screenshots of various pieces of software.

##### During the Workshop

- Separate into teams and cut up each page
- Create subcategories as needed
- Align on names for the components



You can see where and how the ecperience is breaking, and where you'll need to start making these changes.

##### The Component Cut-Up Workshop

- ##### Identify the design problems and extract the best solution to those problems.

- ##### Remove anything that doesn't have a purpose.

- ##### Generates momentum

- ##### Builds early consistency and alignment

  #####  

### 6. Creating a solid foundation

##### Design Components from Scratch

- create the order for when you are going to takle each component.

- Start with color, typography, iconography, units of measure, grids, and spacing.

- Define which pieces inform others.

- Align on what you are going to name each component

  > Define common terms used to refer to each item and name the patterns in an agnostic way to reduce duplication and ensure scalability.




**White down specific reasons  why you made certain design decisions.!!!**

> 1. this helps you rationalize your thinking later and when other people ask you why you made certain design decisions.
> 2. help you write the guideline and documentation foe the components as team members start to utilize parts of the system.



##### Management and Organization

- Schedule weekly reviews with stakeholders and developers

  > 1. you'll need buy-in and validation of ideas from the product donors and the users of the system, 
  > 2. and the developers need to be there to validate designs and make sure that everything is feasible from a development standpoint.


- Establish long-term governace

  > Who maintains the design system going forward?
  >
  > What is the contribution process?
  >
  > How is it going to be shared out?
  >
  > All of these questions are going to need to be answered before the system goes live.
  >
  > Successful design systems are in constant service to many audiences, designers, developers,product managers, the end user. That spirit of service means that keepers pf the systemhave to keep their ego at bay.

**A design system is not a place to push new frontiers but rather to gather settled solutions.**



There's one important thing to consider.

**"A Design System isn't a project. It is a product, serving products."**

> "A design system is not simply a style guide. It is a living thing whose value is realized only when products successfully implement the patterns of the system." 
>
> — Nathan Curtis

It needs to be maintained and allow for growth.



### 7. Collaborate with  others

##### Naming Conventions

- Simple and consistent
- Alphanumeric characters only (a-z 0-9)
- No special characters (,./\@#$%{}_+-)
- No Spaces
- To seperate words:
  - Use underscore (about_us) or
  - Use camel case (aboutUs)

(Naming objects helps with CSS coding)



















# Design System Part 2

### Color

##### Choosing ghe right colors

accessibility. maintain reasonable contrast ratios between text and background colors, the ratio is 4.5:1 for small text, 3:1 for large text. 



##### Color Wheel

1. Analogous
2. ​





### Typography

> **Early days of the web**
>
> - Limited font options
> - Readability & Avaliability
> - "Websafe" fonts
>
> **Modern web design**
>
> - Many more font choices
> - Font embedding
> - Font hosting services

##### 1. Define font setting

- font-size
- lineheight
- letterspacing
- color
- font-family

##### 2. Define HTML typography elements

##### 3. Special HTML elements

- Blockquote
- Caption
- Lists



### Grid







### Iconography

##### SVG

A vector graphic format that can scale to any size without losing clarity. require fall back for older browsers.



##### Icon Font

Icon fonts are mapped to individual unicode characters, enabling you to store multiple icons within a single file. Fonts are vectors so icons can scale to any size.

work well when using a large number of icons with basic styling requirements.








# - Design Example -

###### Principles 设计原则



## === MOTION ===



## === FOUNDATIONS ===

##### Color 色彩

##### Icons 图标

##### Typography 字体

##### Writing 文案

##### Layout 布局 

###### Grid

###### Layout

尺寸、最小宽度



## === COMPONENTS ===

##### 

##### Button 按钮



### --- Navigation ---

##### Affix 固钉

##### Breadcrumb 面包屑

##### Dropdown 下拉菜单

##### Menu 导航菜单

##### Pagination 分页

##### Stepper 步幅器

### --- Feedback ---

##### Alert 警告提示

##### Notification 通知提示

##### Message 全局提示

##### Modal dialog 模式对话框

##### Loading 加载

### — Data Input ---  

##### Text field 文本输入

> 1. Label
> 2. Cursor
> 3. Input text
> 4. Placeholder text (Hint text)
> 5. Helper text
> 6. Error message
> 7. Required field
> 8. Character or word counter
> 9. Icon signifier
> 10. Dropdown icon
> 11. Clear button
> 12. States
>     - Idle
>     - Hover
>     - Pressed
>     - Focused
>     - Empty or filled
>     - Valid or invalid
> 13. Formatted inputs
>     - Grouped characters
>     - Prefixes and suffixes
>     - Password redaction
> 14. Single-line
> 15. Multi-line
> 16. Text area

##### Inline edit (未使用)

> 文本可以实时保存、编辑，不需确认的可以使用此组件

### 

##### DatePicker 日期选择

##### Radio 单选框

##### Checkbox 多选框

##### Switch 开关

##### Select 选择器

1. 下拉选择器
2. single-select
3. menus google
4. TreeSelect 树选择
5. Cascader 级联选择

##### Transfer 穿梭框 (未使用)

##### Upload 上传

### --- Data Display ---  

##### Card卡片

##### Calendar日历 (未使用)

##### Avatar 头像

##### Badge 徽标

##### Table 表格

##### Carousel 走马灯 (未使用)

##### Expansion panel 折叠面板

##### Popover 弹出框（气泡框）

##### Tooltip 工具提示

##### Tabs 标签页

##### Tag 标签

##### Indicator 指示器 (Timeline 时间轴)

1. Timeline时间轴


2. Progress进度条


##### Tree 树形控件



##### 空页面

##### 引导