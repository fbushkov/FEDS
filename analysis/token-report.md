# Отчёт по токенам (генерируется tools/analyze_tokens.py)

- **1. Primitives** — 643 переменных, режимы: Mode 1
- **2. General** — 2261 переменных, режимы: light, dark
- **3. Components** — 1987 переменных, режимы: Mode 1

## Проблемы

### broken-alias: 0

### level-skip-or-upward: 0

### raw-value-above-L1: 2
- `number [light] = 0`
- `number [dark] = 0`

### non-kebab: 0

## Грамматика L3 по компонентам

### avatar (207)
- [3 сегм., 26] avatar / {button-x,icon,status,text} / {away,base,base-inverse,blue,box,busy,counter,description,green,icon,name,notification,offline,online,purple,red,spacer,text,yellow}
- [4 сегм., 181] avatar / {box,box-group,size} / {2xl,border,hard,l,m,s,soft,xl} / {base,blue,box,box-border,box-group-border,box-group-gap,box-icon-plus,box-icon-user,box-radius-circle,box-radius-square,box-text-x,box-text-y-bottom,box-text-y-top,box-xy,button-x,button-x-border,button-x-icon,button-x-radius,button-x-xy,counter,counter-border,counter-radius,counter-x,counter-y-bottom,counter-y-top,focus,focus-border,focus-radius-circle,focus-radius-square,green,hard,inverse,name-box-gap,name-description-gap,purple,red,soft,spacer,spacer-inverse,status,status-border,status-radius,yellow}

### badge (121)
- [3 сегм., 12] badge / {border,status} / {base,base-inverse,blue,focus,green,hard,hard-inverse,purple,red,soft,soft-inverse,yellow}
- [4 сегм., 109] badge / {bg,counter,icon,size,text} / {hard,m,s,soft} / {base,base-inverse,blue,box,box-border,box-gap,box-icon-x,box-icon-y,box-radius-circle,box-radius-square,box-x,box-y,counter,counter-radius,counter-x,counter-y-bottom,counter-y-top,focus-border,focus-radius-circle,focus-radius-square,green,icon,purple,red,status-box,status-icon,status-radius,text-base,text-base-inverse,text-blue,text-green,text-inverse,text-padding,text-purple,text-red,text-yellow,yellow}

### button (333)
- [2 сегм., 1] button / focus-ring
- [4 сегм., 64] button / size / {l,m,s,xl} / {border-fill,border-focus,border-outline,border-text,box,gap,gap-text,icon,radius,radius-focus,radius-text,x,x-icon-button,x-text,y,y-text}
- [5 сегм., 260] button / {fill,outline,text-button} / {danger,danger-soft,ghost,inverse,primary,primary-soft,secondary,tertiary} / {bg,border,icon,text} / {default,disabled,hover,pressed}
- [6 сегм., 8] button / text-button / inverse / icon / {primary,secondary} / {default,disabled,hover,pressed}

### checkbox (110)
- [2 сегм., 1] checkbox / focus-ring
- [3 сегм., 23] checkbox / {card,loading,text,unchecked} / {bg,border,box-checked,box-uncheked,description,disabled,error,icon,inverse-bg,inverse-border,inverse-box-checked,inverse-box-uncheked,inverse-description,inverse-disabled,inverse-icon,inverse-name,name}
- [4 сегм., 44] checkbox / {checked,size,unchecked} / {bg,border,card,icon,inverse-bg,inverse-border,inverse-icon} / {border,default,disabled,error,hover,pressed,radius}
- [5 сегм., 42] checkbox / size / {card,main} / {l,m} / {box,box-border,box-check-y-bottom,box-check-y-top,box-container,box-container-xy,box-icon-x,box-icon-y,box-radius,checkbox-text-gap,focus-border,focus-radius,icon,icon-text,text-container-x,text-container-y,text-interline-gap,x,y-bottom,y-top}

### chip (213)
- [3 сегм., 1] chip / border / focus
- [4 сегм., 72] chip / {icon,size} / {hard,hard-disabled,m,s,soft,soft-disabled} / {base,base-inverse,blue,box,box-avatar-x,box-avatar-y,box-border,box-gap,box-radius-circle,box-radius-square,box-x,box-y,counter-gap,counter-x,counter-y-bottom,counter-y-top,focus-border,focus-radius-circle,focus-radius-square,green,icon,purple,red,text-avatar-x,text-gap,text-x,text-y-bottom,text-y-top,yellow}
- [5 сегм., 140] chip / {bg,border,text} / {hard,soft} / {base,base-inverse,blue,disabled,green,main,purple,red,secondary,yellow} / {active,base,base-inverse,blue,default,disabled,green,hover,purple,red,yellow}

### divider (44)
- [3 сегм., 7] divider / {label,line} / {dark,intense,light,middle,regular,strong,subtle}
- [4 сегм., 29] divider / size / {m,padding,s,xs} / {12,16,20,24,32,4,40,8,border,box,gap,radius-circle,radius-none,x,y}
- [5 сегм., 8] divider / size / label / {m,s} / {box,x,y-bottom,y-top}

### field (514)
- [3 сегм., 14] field / {counter,label,select} / {additional,focus-ring,inverse-additional,inverse-focus-ring,inverse-over-limit,inverse-primary,inverse-regular,inverse-requirement,inverse-secondary,over-limit,primary,regular,requirement,secondary}
- [4 сегм., 122] field / {description,input,select} / {bg,border,icon,leading,leading-icon,loading,text,validation-icons} / {caret,default,disabled,error,focused,hint,hover,icon,inactive,inactive-disabled,inverse-caret,inverse-default,inverse-disabled,inverse-error,inverse-focused,inverse-hint,inverse-hover,inverse-icon,inverse-inactive,inverse-inactive-disabled,inverse-loading,inverse-placeholder,inverse-pressed,inverse-read-only,inverse-resizer,inverse-success,inverse-text,inverse-value,inverse-warning,loading,placeholder,pressed,read-only,resizer,success,text,value,warning}
- [5 сегм., 207] field / {select,size} / {description,dropdown,field,input,label,select,text-area} / {container,extraspace,l,m,s} / {actions,actions-xy,additional-x-left,additional-x-right,additional-y,base,border,button-dropdown-gap,caret-box-height,caret-box-width,caret-height,caret-radius,caret-width,container,container-x,container-y,counter,gap-container,gap-horizontal,gap-icon-text,gap-leading,gap-left-right,gap-text,gap-text-asterisk,gap-text-link,gap-trailing,gap-vertical,height,hint,hint-icon,hint-icon-box,hint-icon-x,hint-icon-y,horizontal,horizontal-y,info-box,info-icon-xy,inverse-base,inverse-hint,inverse-loader-icon,l,leading-icon,leading-icon-box,leading-icon-xy,loader-icon,loading-icon,loading-icon-box,loading-icon-xy,m,prefix-x-left,prefix-x-right,prefix-y,radius,requirement,resizer,resizer-box,s,suffix-x-left,suffix-x-right,suffix-y,text-x-left,text-x-right,text-y,validation-icon,validation-icon-box,validation-icon-xy,x-left,x-right,y-bottom,y-top}
- [6 сегм., 171] field / {select,size} / {dropdown,field,select} / {base,l,m,option,s} / {bg,button,divider,dropdown-box,indicator,l,leading-icon,m,option,s,text} / {action-box,action-xy,active,active-disabled,active-hover,container,container-border,container-gap,container-radius,container-x,container-y,default,disabled,focus-border,focus-radius,gap,gap-horizontal,gap-vertical,hover,icon,icon-disabled,indicator-icon,indicator-icon-box,indicator-icon-xy,inverse,inverse-active,inverse-active-disabled,inverse-active-hover,inverse-default,inverse-disabled,inverse-hover,inverse-icon,inverse-icon-disabled,inverse-pressed,inverse-read-only,inverse-value,leading-icon,leading-icon-box,leading-icon-xy,loader,loading-icon,loading-icon-box,loading-icon-xy,pressed,read-only,text-gap,text-x-left,text-x-right,text-y,trailing-gap,validation-icon,validation-icon-box,validation-icon-xy,value,x-left,x-right,y-bottom,y-top}

### link (60)
- [2 сегм., 1] link / focus-ring
- [4 сегм., 59] link / {danger,main,secondary,size} / {icon,l,m,s,text,xl} / {box,default,disabled,focus-border,focus-radius,gap,hover,icon,pressed,radius,visited,x,y}

### priority-indicator (66)
- [2 сегм., 1] priority-indicator / focus
- [3 сегм., 15] priority-indicator / {bg,icon,text} / {base,blocker,critical,high,low,medium,minor,none}
- [4 сегм., 50] priority-indicator / size / {m,s} / {box,box-icon,box-icon-gap,box-icon-monochrome-x,box-icon-monochrome-y,box-icon-radius,box-icon-x,box-icon-y,box-radius,box-x,box-y,container-icon-x,container-icon-y,container-text-x,container-text-y,custom-box-gap,custom-box-x,custom-box-y,focus-border,focus-radius,icon,icon-blocker,icon-blocker-box-x,icon-blocker-box-y,icon-gap}

### radiobutton (106)
- [2 сегм., 1] radiobutton / focus-ring
- [3 сегм., 23] radiobutton / {card,loading,text,unchecked} / {bg,border,box-checked,box-uncheked,description,disabled,error,icon,inverse-bg,inverse-border,inverse-box-checked,inverse-box-uncheked,inverse-description,inverse-disabled,inverse-icon,inverse-name,name}
- [4 сегм., 44] radiobutton / {checked,size,unchecked} / {bg,border,card,icon,inverse-bg,inverse-border,inverse-icon} / {border,default,disabled,error,hover,pressed,radius}
- [5 сегм., 38] radiobutton / size / {card,main} / {l,m} / {box,box-border,box-container,box-container-xy,box-radius,box-xy,focus-border,focus-radius,icon,icon-radius,icon-text,radio-text-gap,text-container-x,text-container-y,text-interline-gap,x,y-bottom,y-top}

### status (91)
- [3 сегм., 5] status / {loading,text} / {icon,inverse,inverse-icon,inverse-name,name}
- [4 сегм., 86] status / {bg,icon,size,text} / {hard,l,m,soft,status} / {avatar-box,box,box-gap,box-icon-x,box-radius-circle,box-radius-square,box-x,box-y,brand,dot,error,icon,icon-box,info,inverse-neutral,marker,marker-radius,neutral,pending,success,unboxed,unboxed-gap,unboxed-radius,unboxed-x,unboxed-y,warning}

### switch (122)
- [2 сегм., 1] switch / focus-ring
- [3 сегм., 21] switch / {card,loading,off,text} / {bg,border,box-off,box-on,description,disabled,error,icon,inverse-bg,inverse-border,inverse-box-off,inverse-box-on,inverse-description,inverse-disabled,inverse-icon,inverse-name,name}
- [4 сегм., 56] switch / {off,on,size} / {bg,border,card,icon,inverse-bg,inverse-border,knob} / {border,default,disabled,error,hover,inverse-disabled,pressed,radius}
- [5 сегм., 44] switch / size / {card,main} / {l,m} / {box-border,box-height,box-radius,box-width,box-x,box-y,control-text-gap,focus-border,focus-radius,icon,icon-text,knob,knob-pending,knob-radius,knob-xy,text-container-x,text-container-y,text-interline-gap,x,y-bottom,y-top}

## Грамматика L2 (корни)

- [29] border / avatar / {box,box-group,button-x,counter,focus,status} / {2xl,l,m,s,xl}
- [4] border / badge / {box,focus} / {m,s}
- [5] border / button / {fill,focus-bold,focus-regular,none,outline}
- [1] border / checkbox / card
- [4] border / checkbox / {box,focus} / {l,m}
- [4] border / chip / {box,focus} / {m,s}
- [3] border / divider / {l,m,s}
- [3] border / field / input / {l,m,s}
- [6] border / field / select / {button,focus} / {l,m,s}
- [2] border / link / {focus-bold,focus-regular}
- [2] border / priority-indicator / focus / {m,s}
- [1] border / radiobutton / card
- [4] border / radiobutton / {box,focus} / {l,m}
- [1] border / switch / card
- [4] border / switch / {box,focus} / {l,m}
- [400] color / action / {bg,border,indicator,text} / {base,brand,danger,info,success,warning} / {calm,controls,firm,ghost,hard,inverse,inverse-controls,inverse-ghost,inverse-hard,inverse-light,inverse-medium,inverse-pure,inverse-quiet,inverse-soft,light,medium,plain,pure,quiet,soft} / {brand,default,disabled,hover,inverse-selected,pressed,read-only,selected,visited}
- [33] color / bg / {overlay,page,raised,section} / {brand-soft,brand-weak,green-light,green-soft,green-weak,hard,inverse-brand-weak,inverse-main,inverse-medium,inverse-secondary,inverse-tertiary,light,low,main,medium,red-main,red-soft,red-weak,secondary,tertiary}
- [35] color / static / {divider,focus} / {base-plain,brand,brand-quiet,calm,danger,firm,hard,heavy,info,inverse-base-plain,inverse-brand,inverse-calm,inverse-danger,inverse-firm,inverse-hard,inverse-heavy,inverse-info,inverse-light,inverse-low,inverse-medium,inverse-mild,inverse-plain,inverse-soft,inverse-strong,inverse-success,inverse-warning,light,low,medium,mild,plain,soft,strong,success,warning}
- [186] color / static / {border,indicator,text} / {base,brand,context,danger,info,palette,success,warning} / {away,blue,blue-hard,blue-low,blue-medium,busy,calm,danger,firm,green,green-hard,green-low,green-medium,grey-hard,grey-low,grey-medium,hard,inverse-away,inverse-busy,inverse-calm,inverse-danger,inverse-firm,inverse-hard,inverse-light,inverse-low,inverse-medium,inverse-mild,inverse-notification,inverse-offline,inverse-online,inverse-plain,inverse-quiet,inverse-soft,inverse-success,inverse-warning,inverse-weak,light,low,medium,mild,notification,offline,online,plain,purple,purple-hard,purple-low,purple-medium,quiet,red,red-hard,red-low,red-medium,soft,success,warning,weak,yellow,yellow-hard,yellow-low,yellow-medium}
- [57] color / static / bg / {solid,transparent} / {base,blue,brand,green,purple,red,yellow} / {deep,ghost,hard,heavy,inverse-hard,inverse-heavy,inverse-light,inverse-medium,inverse-mild,inverse-pure,inverse-quiet,inverse-weak,light,low,medium,mild,plain,pure,quiet,soft,strong,weak}
- [25] color / static / bg / transparent / accent / {blue,brand,green,purple,red,yellow} / {light,low,medium,quiet,soft}
- [173] color / status / {base,blue,brand,green,purple,red,yellow} / {ghost,hard,heavy,inverse-soft,light,medium,pure,quiet,soft,weak} / {active,border,border-active,border-disabled,border-hover,default,hover,on,on-brand,on-secondary}
- [5] color / surface / brand / {default,disabled,hover,pressed,selected}
- [35] color / surface / base / {ghost,hard,inverse-ghost,inverse-pure,pure,soft,weak} / {default,disabled,hover,pressed,selected}
- [12] effects / select / {blur,spread,x,y} / {l,m,s}
- [8] effects / switch / knob / {blur,spread,x,y} / {l,m}
- [14] gap / avatar / {box-group,box-name,name-description} / {2xl,l,m,s,xl}
- [2] gap / badge / {m,s}
- [10] gap / button / {l,l-text,m,m-text,none,s,s-text,xl,xl-text,xs-text}
- [4] gap / checkbox / {checkbox-text,text-interline} / {l,m}
- [6] gap / chip / {m,m-counter,m-text,s,s-counter,s-text}
- [3] gap / divider / {m,s,xs}
- [6] gap / field / {horizontal,vertical} / {l,m,s}
- [51] gap / field / {description,input,label,select} / {button,button-dropdown,container,dropdown,horizontal,icon-text,leading,left-right,option,text,text-asterisk,text-link,trailing,vertical} / {l,m,s}
- [4] gap / link / {l,m,s,xl}
- [6] gap / priority-indicator / {m-custom,m-icon,m-icon-box,s-custom,s-icon,s-icon-box}
- [4] gap / radiobutton / {radio-text,text-interline} / {l,m}
- [4] gap / status / {box,unboxed} / {l,m}
- [4] gap / switch / {control-text,text-interline} / {l,m}
- [5] radius / avatar / {box,button-x,counter,focus,status} / circle
- [10] radius / avatar / {box,focus} / square / {2xl,l,m,s,xl,xs}
- [8] radius / badge / {box,counter,focus,status} / {circle,m,m-square,s,s-square}
- [4] radius / button / {l,m,s,xl}
- [5] radius / button / focus / {l,m,none,s,xl}
- [1] radius / checkbox / card
- [4] radius / checkbox / {box,focus} / {l,m}
- [6] radius / chip / {box,focus} / {circle,m,m-square,s,s-square}
- [2] radius / divider / {circle,none}
- [6] radius / field / {caret,input} / {l,m,s}
- [9] radius / field / select / {button,focus,option} / {l,m,s}
- [1] radius / link / box
- [4] radius / link / focus / {l,m,s,xl}
- [6] radius / priority-indicator / {box,focus} / {m,m-icon,s,s-icon}
- [4] radius / radiobutton / {box,card,focus,icon}
- [5] radius / status / {circle,icon-marker,l-square,m-square,unboxed}
- [4] radius / switch / {box,card,focus,knob}
- [33] size / avatar / {box,button-x,counter,icon-plus,icon-user,status} / {2xl,2xl-icon,l,l-icon,m,m-icon,s,xl,xl-icon}
- [10] size / badge / {box,counter,icon,status} / {m,m-box,m-icon,s,s-box,s-icon}
- [8] size / button / {l,l-icon,m,m-icon,s,s-icon,xl,xl-icon}
- [4] size / checkbox / {box,box-container} / {l,m}
- [4] size / checkbox / icon / {card,check} / {l,m}
- [4] size / chip / {box,icon} / {m,s}
- [13] size / divider / {label,padding,thickness} / {12,16,20,24,32,4,40,8,l,m,s}
- [6] size / field / {counter,extraspace} / {l,m,s}
- [36] size / field / {hint-icon,input,label,resizer,select} / {action,actions,box,button,container,height,horizontal,icon,info-box,requirement} / {l,l-width,m,m-width,s,s-width}
- [54] size / field / {input,select} / {caret,leading,loading,option,validation-markers} / {box,container,icon,icon-box,loader} / {l,l-height,l-width,m,m-height,m-width,s,s-height,s-width}
- [12] size / field / select / option / {indicator,leading} / {icon,icon-box} / {l,m,s}
- [8] size / link / {l,l-icon,m,m-icon,s,s-icon,xl,xl-icon}
- [8] size / priority-indicator / {box,icon} / {m,m-blocker,m-icon,s,s-blocker,s-icon}
- [4] size / radiobutton / {box,box-container} / {l,m}
- [4] size / radiobutton / icon / {card,radio} / {l,m}
- [14] size / status / {avatar-box,box,dot,icon,icon-box,marker,unboxed} / {l,m}
- [8] size / switch / {box,knob} / {l,l-height,l-pending,l-width,m,m-height,m-pending,m-width}
- [4] size / switch / icon / {card,status} / {l,m}
- [4] space / avatar / button-x / {xy-2xl,xy-l,xy-m,xy-xl}
- [17] space / avatar / {box,counter} / {x,xy,y} / {2xl,2xl-bottom,2xl-top,l,l-bottom,l-top,m,m-bottom,m-top,s,xl,xl-bottom,xl-top}
- [15] space / avatar / box / text / {x,y} / {2xl,2xl-bottom,2xl-top,l,l-bottom,l-top,m,m-bottom,m-top,s,s-bottom,s-top,xl,xl-bottom,xl-top}
- [2] space / badge / text / {m-x,s-x}
- [14] space / badge / {box,counter} / {x,y} / {m,m-bottom,m-icon,m-top,s,s-bottom,s-icon,s-top}
- [14] space / button / {x,y} / {l,l-icon,m,m-icon,s,s-icon,text,xl,xl-icon}
- [2] space / checkbox / container / {xy-l,xy-m}
- [20] space / checkbox / {box,card,text-container} / {x,y} / {l,l-bottom,l-check-bottom,l-check-top,l-icon-text,l-top,m,m-bottom,m-check-bottom,m-check-top,m-icon-text,m-top}
- [22] space / chip / {box,counter,text} / {x,y} / {m,m-avatar,m-bottom,m-top,s,s-avatar,s-bottom,s-top}
- [12] space / divider / {box,label} / {x,y} / {m,m-bottom,m-top,s,s-bottom,s-top,xs}
- [42] space / field / {base,input,label,select} / {action,actions,horizontal-y,info-box,leading-icon,loading-icon,validation-icon,x,y} / {l,l-bottom,l-left,l-right,l-top,m,m-bottom,m-left,m-right,m-top,s,s-bottom,s-left,s-right,s-top}
- [99] space / field / {description,input,label,select} / {additional,base,button,container,dropdown,hint-icon,option,prefix,suffix,text} / {indicator,leading-icon,x,y} / {l,l-bottom,l-left,l-right,l-top,m,m-bottom,m-left,m-right,m-top,s,s-bottom,s-left,s-right,s-top}
- [15] space / field / select / option / {container,text} / {x,y} / {l,l-left,l-right,m,m-left,m-right,s,s-left,s-right}
- [8] space / link / {x,y} / {l,m,s,xl}
- [28] space / priority-indicator / {box,container,icon} / {x,y} / {m,m-blocker,m-colored,m-custom,m-icon,m-monohrome,m-text,s,s-blocker,s-colored,s-custom,s-icon,s-monohrome,s-text}
- [4] space / radiobutton / {box,container} / {xy-l,xy-m}
- [12] space / radiobutton / {card,text-container} / {x,y} / {l,l-bottom,l-icon-text,l-top,m,m-bottom,m-icon-text,m-top}
- [10] space / status / box / {x,y} / {l,l-icon,l-unboxed,m,m-icon,m-unboxed}
- [2] space / switch / knob / {xy-l,xy-m}
- [16] space / switch / {box,card,text-container} / {x,y} / {l,l-bottom,l-icon-text,l-top,m,m-bottom,m-icon-text,m-top}
- [88] typography / avatar / {2xl,l,m,s,xl} / {counter,description,initials,more,name} / {letter-spacing,line-height,size,weight}
- [16] typography / badge / {m,s} / {counter,name} / {letter-spacing,line-height,size,weight}
- [16] typography / button / {l,m,s,xl} / {letter-spacing,line-height,size,weight}
- [16] typography / checkbox / {l,m} / {description,name} / {letter-spacing,line-height,size,weight}
- [24] typography / chip / {m,s} / {description,head,name} / {letter-spacing,line-height,size,weight}
- [4] typography / content / title / {letter-spacing,line-height,size,weight}
- [28] typography / content / {body,label} / {caption,default,large,strong} / {letter-spacing,line-height,size,weight}
- [8] typography / divider / {m,s} / {letter-spacing,line-height,size,weight}
- [24] typography / field / {counter,hint} / {l,m,s} / {letter-spacing,line-height,size,weight}
- [108] typography / field / {input,label,select} / {additional,hint,option,option-title,prefix,suffix,text,title} / {l,m,s} / {letter-spacing,line-height,size,weight}
- [16] typography / link / {l,m,s,xl} / {letter-spacing,line-height,size,weight}
- [12] typography / page / {caption,default,title} / {letter-spacing,line-height,size,weight}
- [8] typography / priority-indicator / {m,s} / {letter-spacing,line-height,size,weight}
- [16] typography / radiobutton / {l,m} / {description,name} / {letter-spacing,line-height,size,weight}
- [16] typography / section / {caption,default,overline,title} / {letter-spacing,line-height,size,weight}
- [8] typography / status / {l,m} / {letter-spacing,line-height,size,weight}
- [16] typography / switch / {l,m} / {description,name} / {letter-spacing,line-height,size,weight}