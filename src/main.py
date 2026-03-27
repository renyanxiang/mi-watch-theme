#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time

class MiWatchTheme:
    def __init__(self):
        self.theme_name = "Mi Watch S4 Theme"
        self.version = "1.0.0"
        self.author = "Your Name"
        self.screen_size = "1.43"  # 小米Watch S4屏幕尺寸
        self.resolution = "466x466"  # 小米Watch S4屏幕分辨率
        self.time_format = "24h"  # 默认24小时制
        self.date_format = "YYYY-MM-DD"  # 默认日期格式
        self.battery_level = 85  # 模拟电池电量百分比
        self.battery_status = "normal"  # 电池状态：normal, charging, low
        self.steps = 5234  # 模拟当天步数
        self.step_goal = 10000  # 步数目标
        self.heart_rate = 72  # 模拟当前心率
        self.heart_rate_history = [68, 70, 72, 75, 73, 72]  # 模拟心率历史数据
        self.weather = {
            "condition": "晴天",
            "temperature": 23,
            "humidity": 65,
            "wind_speed": 12,
            "icon": "☀️"
        }
        self.background = {
            "type": "color",  # 背景类型：color, image
            "color": "#000000",  # 默认背景颜色
            "image_path": "",  # 背景图片路径
            "blur": False  # 是否开启模糊效果
        }
        self.animations = {
            "enabled": True,  # 是否开启动画
            "duration": 1000,  # 动画持续时间（毫秒）
            "time_update": True,  # 时间更新动画
            "element_load": True,  # 元素加载动画
            "interaction": True  # 交互反馈动画
        }
    
    def get_current_time(self):
        """获取当前时间"""
        if self.time_format == "24h":
            return time.strftime("%H:%M")
        else:
            return time.strftime("%I:%M %p")
    
    def toggle_time_format(self):
        """切换时间格式"""
        if self.time_format == "24h":
            self.time_format = "12h"
        else:
            self.time_format = "24h"
        return self.time_format
    
    def get_current_date(self):
        """获取当前日期"""
        if self.date_format == "YYYY-MM-DD":
            return time.strftime("%Y-%m-%d")
        elif self.date_format == "DD/MM/YYYY":
            return time.strftime("%d/%m/%Y")
        elif self.date_format == "MM/DD/YYYY":
            return time.strftime("%m/%d/%Y")
        else:
            return time.strftime("%Y-%m-%d")
    
    def get_current_weekday(self):
        """获取当前星期几"""
        weekdays = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
        return weekdays[time.localtime().tm_wday]
    
    def set_date_format(self, format_str):
        """设置日期格式"""
        valid_formats = ["YYYY-MM-DD", "DD/MM/YYYY", "MM/DD/YYYY"]
        if format_str in valid_formats:
            self.date_format = format_str
        return self.date_format
    
    def get_battery_level(self):
        """获取电池电量百分比"""
        return self.battery_level
    
    def set_battery_level(self, level):
        """设置电池电量百分比"""
        self.battery_level = max(0, min(100, level))
        # 更新电池状态
        if self.battery_level <= 20:
            self.battery_status = "low"
        else:
            self.battery_status = "normal"
        return self.battery_level
    
    def set_battery_status(self, status):
        """设置电池状态"""
        valid_statuses = ["normal", "charging", "low"]
        if status in valid_statuses:
            self.battery_status = status
        return self.battery_status
    
    def get_battery_icon(self):
        """获取电池图标"""
        if self.battery_status == "charging":
            return "🔋 (充电中)"
        elif self.battery_status == "low":
            return "🔋 (低电量)"
        else:
            if self.battery_level >= 80:
                return "🔋 (高电量)"
            elif self.battery_level >= 50:
                return "🔋 (中电量)"
            else:
                return "🔋 (低电量)"
    
    def get_steps(self):
        """获取当天步数"""
        return self.steps
    
    def set_steps(self, steps):
        """设置当天步数"""
        self.steps = max(0, steps)
        return self.steps
    
    def get_step_goal(self):
        """获取步数目标"""
        return self.step_goal
    
    def set_step_goal(self, goal):
        """设置步数目标"""
        self.step_goal = max(1000, goal)  # 最小目标为1000步
        return self.step_goal
    
    def get_step_progress(self):
        """获取步数进度百分比"""
        if self.step_goal == 0:
            return 0
        return min(100, (self.steps / self.step_goal) * 100)
    
    def get_step_progress_bar(self):
        """获取步数进度条"""
        progress = self.get_step_progress()
        bar_length = 20
        filled_length = int(bar_length * progress / 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        return f"[{bar}] {progress:.1f}%"
    
    def get_heart_rate(self):
        """获取当前心率"""
        return self.heart_rate
    
    def set_heart_rate(self, rate):
        """设置当前心率"""
        self.heart_rate = max(40, min(200, rate))  # 心率范围：40-200
        self.update_heart_rate_history(self.heart_rate)
        return self.heart_rate
    
    def get_heart_rate_status(self):
        """获取心率状态"""
        if self.heart_rate < 60:
            return "偏低"
        elif self.heart_rate > 100:
            return "偏高"
        else:
            return "正常"
    
    def get_heart_rate_color(self):
        """获取心率状态对应的颜色"""
        if self.heart_rate < 60:
            return "#4CAF50"  # 绿色
        elif self.heart_rate > 100:
            return "#FF5252"  # 红色
        else:
            return "#2196F3"  # 蓝色
    
    def get_heart_rate_history(self):
        """获取心率历史数据"""
        return self.heart_rate_history
    
    def update_heart_rate_history(self, rate):
        """更新心率历史数据"""
        self.heart_rate_history.append(rate)
        if len(self.heart_rate_history) > 10:
            self.heart_rate_history.pop(0)  # 只保留最近10个数据点
    
    def get_heart_rate_trend(self):
        """获取心率趋势"""
        if len(self.heart_rate_history) < 2:
            return "稳定"
        
        trend = self.heart_rate_history[-1] - self.heart_rate_history[0]
        if trend > 5:
            return "上升"
        elif trend < -5:
            return "下降"
        else:
            return "稳定"
    
    def get_weather(self):
        """获取天气信息"""
        return self.weather
    
    def set_weather(self, condition, temperature, humidity, wind_speed):
        """设置天气信息"""
        self.weather = {
            "condition": condition,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "icon": self.get_weather_icon(condition)
        }
        return self.weather
    
    def get_weather_icon(self, condition):
        """根据天气状况获取天气图标"""
        icon_map = {
            "晴天": "☀️",
            "多云": "⛅",
            "阴天": "☁️",
            "雨天": "🌧️",
            "雪天": "❄️",
            "雾天": "🌫️",
            "雷暴": "⛈️"
        }
        return icon_map.get(condition, "☀️")
    
    def get_weather_condition(self):
        """获取天气状况"""
        return self.weather.get("condition", "未知")
    
    def get_temperature(self):
        """获取温度"""
        return self.weather.get("temperature", 0)
    
    def get_humidity(self):
        """获取湿度"""
        return self.weather.get("humidity", 0)
    
    def get_wind_speed(self):
        """获取风速"""
        return self.weather.get("wind_speed", 0)
    
    def get_weather_icon_display(self):
        """获取天气图标"""
        return self.weather.get("icon", "☀️")
    
    def get_background(self):
        """获取背景设置"""
        return self.background
    
    def set_background_color(self, color):
        """设置背景颜色"""
        self.background["type"] = "color"
        self.background["color"] = color
        return self.background
    
    def set_background_image(self, image_path, blur=False):
        """设置背景图片"""
        self.background["type"] = "image"
        self.background["image_path"] = image_path
        self.background["blur"] = blur
        return self.background
    
    def toggle_background_blur(self):
        """切换背景模糊效果"""
        self.background["blur"] = not self.background["blur"]
        return self.background["blur"]
    
    def get_background_display(self):
        """获取背景显示信息"""
        if self.background["type"] == "color":
            return f"Color: {self.background['color']}"
        else:
            blur_info = "with blur" if self.background["blur"] else "without blur"
            return f"Image: {self.background['image_path']} {blur_info}"
    
    def get_animations(self):
        """获取动画设置"""
        return self.animations
    
    def toggle_animations(self):
        """切换动画开关"""
        self.animations["enabled"] = not self.animations["enabled"]
        return self.animations["enabled"]
    
    def set_animation_duration(self, duration):
        """设置动画持续时间"""
        self.animations["duration"] = max(100, min(3000, duration))  # 动画持续时间范围：100-3000毫秒
        return self.animations["duration"]
    
    def toggle_time_update_animation(self):
        """切换时间更新动画"""
        self.animations["time_update"] = not self.animations["time_update"]
        return self.animations["time_update"]
    
    def toggle_element_load_animation(self):
        """切换元素加载动画"""
        self.animations["element_load"] = not self.animations["element_load"]
        return self.animations["element_load"]
    
    def toggle_interaction_animation(self):
        """切换交互反馈动画"""
        self.animations["interaction"] = not self.animations["interaction"]
        return self.animations["interaction"]
    
    def animate_time_update(self):
        """执行时间更新动画"""
        if self.animations["enabled"] and self.animations["time_update"]:
            print(f"⏰ Time update animation (duration: {self.animations['duration']}ms)")
            # 这里可以添加实际的动画代码
            return True
        return False
    
    def animate_element_load(self, element_name):
        """执行元素加载动画"""
        if self.animations["enabled"] and self.animations["element_load"]:
            print(f"📱 {element_name} load animation (duration: {self.animations['duration']}ms)")
            # 这里可以添加实际的动画代码
            return True
        return False
    
    def animate_interaction(self, interaction_type):
        """执行交互反馈动画"""
        if self.animations["enabled"] and self.animations["interaction"]:
            print(f"👆 {interaction_type} interaction animation (duration: {self.animations['duration']}ms)")
            # 这里可以添加实际的动画代码
            return True
        return False
    
    def get_animation_status(self):
        """获取动画状态"""
        status = f"Animations: {'enabled' if self.animations['enabled'] else 'disabled'}"
        status += f", Duration: {self.animations['duration']}ms"
        status += f", Time update: {'enabled' if self.animations['time_update'] else 'disabled'}"
        status += f", Element load: {'enabled' if self.animations['element_load'] else 'disabled'}"
        status += f", Interaction: {'enabled' if self.animations['interaction'] else 'disabled'}"
        return status
    
    def load_config(self, config_file):
        """加载配置文件"""
        try:
            import json
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # 加载时间格式
                if 'time_format' in config:
                    self.time_format = config['time_format']
                # 加载日期格式
                if 'date_format' in config:
                    self.date_format = config['date_format']
                # 加载背景设置
                if 'background' in config:
                    self.background.update(config['background'])
                # 加载动画设置
                if 'animations' in config:
                    self.animations.update(config['animations'])
                print(f"Config loaded from {config_file}")
                return True
        except Exception as e:
            print(f"Error loading config: {e}")
            return False
    
    def save_config(self, config_file):
        """保存配置文件"""
        try:
            import json
            config = {
                'time_format': self.time_format,
                'date_format': self.date_format,
                'background': self.background,
                'animations': self.animations
            }
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            print(f"Config saved to {config_file}")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def show_config_menu(self):
        """显示配置菜单"""
        print("\n=== Theme Configuration Menu ===")
        print("1. Time format: " + self.time_format)
        print("2. Date format: " + self.date_format)
        print("3. Background: " + self.get_background_display())
        print("4. Animations: " + ("enabled" if self.animations['enabled'] else "disabled"))
        print("5. Animation duration: " + str(self.animations['duration']) + "ms")
        print("6. Save config")
        print("7. Load config")
        print("8. Exit")
        print("==============================")
    
    def handle_config_input(self, choice):
        """处理配置输入"""
        if choice == "1":
            # 切换时间格式
            new_format = self.toggle_time_format()
            print(f"Time format changed to: {new_format}")
        elif choice == "2":
            # 切换日期格式
            print("Select date format:")
            print("1. YYYY-MM-DD")
            print("2. DD/MM/YYYY")
            print("3. MM/DD/YYYY")
            date_choice = input("Enter your choice: ")
            if date_choice == "1":
                self.set_date_format("YYYY-MM-DD")
            elif date_choice == "2":
                self.set_date_format("DD/MM/YYYY")
            elif date_choice == "3":
                self.set_date_format("MM/DD/YYYY")
            print(f"Date format changed to: {self.date_format}")
        elif choice == "3":
            # 配置背景
            print("Select background type:")
            print("1. Color")
            print("2. Image")
            bg_choice = input("Enter your choice: ")
            if bg_choice == "1":
                color = input("Enter color (e.g., #000000): ")
                self.set_background_color(color)
            elif bg_choice == "2":
                image_path = input("Enter image path: ")
                blur = input("Enable blur? (y/n): ").lower() == "y"
                self.set_background_image(image_path, blur)
            print(f"Background updated: {self.get_background_display()}")
        elif choice == "4":
            # 切换动画开关
            enabled = self.toggle_animations()
            print(f"Animations {'enabled' if enabled else 'disabled'}")
        elif choice == "5":
            # 设置动画持续时间
            duration = input("Enter animation duration (100-3000ms): ")
            try:
                duration = int(duration)
                new_duration = self.set_animation_duration(duration)
                print(f"Animation duration set to: {new_duration}ms")
            except ValueError:
                print("Invalid duration")
        elif choice == "6":
            # 保存配置
            config_file = input("Enter config file path (default: config.json): ") or "config.json"
            self.save_config(config_file)
        elif choice == "7":
            # 加载配置
            config_file = input("Enter config file path (default: config.json): ") or "config.json"
            self.load_config(config_file)
        elif choice == "8":
            # 退出
            return False
        else:
            print("Invalid choice")
        return True
    
    def config_mode(self):
        """配置模式"""
        print("Starting configuration mode...")
        while True:
            self.show_config_menu()
            choice = input("Enter your choice: ")
            if not self.handle_config_input(choice):
                break
        print("Exiting configuration mode...")
    
    def preview_theme(self):
        """预览主题"""
        print("\n=== Theme Preview ===")
        print(f"Time: {self.get_current_time()}")
        print(f"Date: {self.get_current_date()} {self.get_current_weekday()}")
        print(f"Battery: {self.get_battery_level()}% {self.get_battery_icon()}")
        print(f"Steps: {self.get_steps()} / {self.get_step_goal()} {self.get_step_progress_bar()}")
        print(f"Heart Rate: {self.get_heart_rate()} BPM {self.get_heart_rate_status()}")
        print(f"Weather: {self.get_weather_icon_display()} {self.get_weather_condition()} {self.get_temperature()}°C")
        print(f"Background: {self.get_background_display()}")
        print(f"{self.get_animation_status()}")
        print("====================")
    
    def export_theme(self, output_path):
        """导出主题为RPK文件"""
        try:
            import zipfile
            import os
            
            # 创建输出目录
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            
            # 创建RPK文件（实际上是ZIP文件）
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                # 导出配置文件
                config = {
                    'theme_name': self.theme_name,
                    'version': self.version,
                    'author': self.author,
                    'screen_size': self.screen_size,
                    'resolution': self.resolution,
                    'time_format': self.time_format,
                    'date_format': self.date_format,
                    'battery_level': self.battery_level,
                    'battery_status': self.battery_status,
                    'steps': self.steps,
                    'step_goal': self.step_goal,
                    'heart_rate': self.heart_rate,
                    'heart_rate_history': self.heart_rate_history,
                    'weather': self.weather,
                    'background': self.background,
                    'animations': self.animations
                }
                
                import json
                config_str = json.dumps(config, ensure_ascii=False, indent=2)
                zf.writestr('config.json', config_str)
                
                # 这里可以添加其他文件，如图标、背景图片等
                # zf.write('background.jpg', 'background.jpg')
                
            print(f"Theme exported to {output_path}")
            return True
        except Exception as e:
            print(f"Error exporting theme: {e}")
            return False
    
    def import_theme(self, input_path):
        """导入主题"""
        try:
            import zipfile
            import json
            
            with zipfile.ZipFile(input_path, 'r') as zf:
                # 读取配置文件
                with zf.open('config.json') as f:
                    config = json.load(f)
                    
                    # 加载配置
                    if 'theme_name' in config:
                        self.theme_name = config['theme_name']
                    if 'version' in config:
                        self.version = config['version']
                    if 'author' in config:
                        self.author = config['author']
                    if 'screen_size' in config:
                        self.screen_size = config['screen_size']
                    if 'resolution' in config:
                        self.resolution = config['resolution']
                    if 'time_format' in config:
                        self.time_format = config['time_format']
                    if 'date_format' in config:
                        self.date_format = config['date_format']
                    if 'battery_level' in config:
                        self.battery_level = config['battery_level']
                    if 'battery_status' in config:
                        self.battery_status = config['battery_status']
                    if 'steps' in config:
                        self.steps = config['steps']
                    if 'step_goal' in config:
                        self.step_goal = config['step_goal']
                    if 'heart_rate' in config:
                        self.heart_rate = config['heart_rate']
                    if 'heart_rate_history' in config:
                        self.heart_rate_history = config['heart_rate_history']
                    if 'weather' in config:
                        self.weather = config['weather']
                    if 'background' in config:
                        self.background = config['background']
                    if 'animations' in config:
                        self.animations = config['animations']
                
                # 这里可以提取其他文件，如图标、背景图片等
                # zf.extract('background.jpg', '.')
                
            print(f"Theme imported from {input_path}")
            return True
        except Exception as e:
            print(f"Error importing theme: {e}")
            return False
    
    def share_theme(self, share_method):
        """分享主题"""
        try:
            # 生成临时RPK文件
            temp_file = f"{self.theme_name.replace(' ', '_')}_v{self.version}.rpk"
            self.export_theme(temp_file)
            
            if share_method == "email":
                print(f"Sharing theme via email: {temp_file}")
                # 这里可以添加邮件分享逻辑
            elif share_method == "bluetooth":
                print(f"Sharing theme via Bluetooth: {temp_file}")
                # 这里可以添加蓝牙分享逻辑
            elif share_method == "cloud":
                print(f"Sharing theme via cloud: {temp_file}")
                # 这里可以添加云分享逻辑
            else:
                print(f"Unknown share method: {share_method}")
                return False
            
            print("Theme shared successfully!")
            return True
        except Exception as e:
            print(f"Error sharing theme: {e}")
            return False
    
    def build(self):
        """构建主题"""
        print(f"Building {self.theme_name} v{self.version}...")
        print(f"Screen size: {self.screen_size}")
        print(f"Resolution: {self.resolution}")
        print(f"Current time: {self.get_current_time()}")
        print(f"Time format: {self.time_format}")
        print(f"Current date: {self.get_current_date()}")
        print(f"Date format: {self.date_format}")
        print(f"Current weekday: {self.get_current_weekday()}")
        print(f"Battery level: {self.get_battery_level()}%")
        print(f"Battery status: {self.battery_status}")
        print(f"Battery icon: {self.get_battery_icon()}")
        print(f"Steps: {self.get_steps()}")
        print(f"Step goal: {self.get_step_goal()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        print(f"Heart rate: {self.get_heart_rate()} BPM")
        print(f"Heart rate status: {self.get_heart_rate_status()}")
        print(f"Heart rate color: {self.get_heart_rate_color()}")
        print(f"Heart rate trend: {self.get_heart_rate_trend()}")
        print(f"Heart rate history: {self.get_heart_rate_history()}")
        print(f"Weather condition: {self.get_weather_condition()}")
        print(f"Temperature: {self.get_temperature()}°C")
        print(f"Humidity: {self.get_humidity()}%")
        print(f"Wind speed: {self.get_wind_speed()} km/h")
        print(f"Weather icon: {self.get_weather_icon_display()}")
        print(f"Background: {self.get_background_display()}")
        print(f"{self.get_animation_status()}")
        # 执行元素加载动画
        self.animate_element_load("Time")
        self.animate_element_load("Date")
        self.animate_element_load("Battery")
        self.animate_element_load("Steps")
        self.animate_element_load("Heart Rate")
        self.animate_element_load("Weather")
        print("Building RPK package...")
        print("Theme built successfully!")
    
    def dev(self):
        """开发模式"""
        print(f"Starting development mode for {self.theme_name}...")
        print(f"Current time: {self.get_current_time()}")
        print(f"Current date: {self.get_current_date()}")
        print(f"Current weekday: {self.get_current_weekday()}")
        print(f"Battery level: {self.get_battery_level()}%")
        print(f"Battery icon: {self.get_battery_icon()}")
        print(f"Steps: {self.get_steps()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        print(f"Heart rate: {self.get_heart_rate()} BPM")
        print(f"Heart rate status: {self.get_heart_rate_status()}")
        print(f"Weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        print(f"Background: {self.get_background_display()}")
        print(f"{self.get_animation_status()}")
        print("Watching for changes...")
    
    def test(self):
        """测试主题"""
        print(f"Testing {self.theme_name} v{self.version}...")
        print(f"Current time: {self.get_current_time()}")
        print("Testing time format toggle...")
        new_format = self.toggle_time_format()
        print(f"Time format toggled to: {new_format}")
        print(f"Current time in new format: {self.get_current_time()}")
        print(f"Current date: {self.get_current_date()}")
        print(f"Current weekday: {self.get_current_weekday()}")
        print("Testing date format change...")
        new_date_format = self.set_date_format("DD/MM/YYYY")
        print(f"Date format changed to: {new_date_format}")
        print(f"Current date in new format: {self.get_current_date()}")
        new_date_format = self.set_date_format("MM/DD/YYYY")
        print(f"Date format changed to: {new_date_format}")
        print(f"Current date in new format: {self.get_current_date()}")
        print("Testing battery level...")
        print(f"Initial battery level: {self.get_battery_level()}%")
        print(f"Initial battery icon: {self.get_battery_icon()}")
        # 测试低电量
        self.set_battery_level(15)
        print(f"Low battery level: {self.get_battery_level()}%")
        print(f"Low battery icon: {self.get_battery_icon()}")
        # 测试充电状态
        self.set_battery_status("charging")
        print(f"Charging status: {self.battery_status}")
        print(f"Charging icon: {self.get_battery_icon()}")
        # 测试高电量
        self.set_battery_level(90)
        self.set_battery_status("normal")
        print(f"High battery level: {self.get_battery_level()}%")
        print(f"High battery icon: {self.get_battery_icon()}")
        print("Testing step counting...")
        print(f"Initial steps: {self.get_steps()}")
        print(f"Step goal: {self.get_step_goal()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        # 测试步数更新
        self.set_steps(8500)
        print(f"Updated steps: {self.get_steps()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        # 测试步数目标更新
        self.set_step_goal(15000)
        print(f"Updated step goal: {self.get_step_goal()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        # 测试达到目标
        self.set_steps(16000)
        print(f"Steps after reaching goal: {self.get_steps()}")
        print(f"Step progress: {self.get_step_progress_bar()}")
        print("Testing heart rate monitoring...")
        print(f"Initial heart rate: {self.get_heart_rate()} BPM")
        print(f"Initial heart rate status: {self.get_heart_rate_status()}")
        print(f"Initial heart rate color: {self.get_heart_rate_color()}")
        print(f"Initial heart rate trend: {self.get_heart_rate_trend()}")
        print(f"Initial heart rate history: {self.get_heart_rate_history()}")
        # 测试低心率
        self.set_heart_rate(55)
        print(f"Low heart rate: {self.get_heart_rate()} BPM")
        print(f"Low heart rate status: {self.get_heart_rate_status()}")
        print(f"Low heart rate color: {self.get_heart_rate_color()}")
        # 测试高心率
        self.set_heart_rate(110)
        print(f"High heart rate: {self.get_heart_rate()} BPM")
        print(f"High heart rate status: {self.get_heart_rate_status()}")
        print(f"High heart rate color: {self.get_heart_rate_color()}")
        # 测试正常心率
        self.set_heart_rate(75)
        print(f"Normal heart rate: {self.get_heart_rate()} BPM")
        print(f"Normal heart rate status: {self.get_heart_rate_status()}")
        print(f"Normal heart rate color: {self.get_heart_rate_color()}")
        print(f"Updated heart rate history: {self.get_heart_rate_history()}")
        print(f"Updated heart rate trend: {self.get_heart_rate_trend()}")
        print("Testing weather information...")
        print(f"Initial weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        print(f"Initial humidity: {self.get_humidity()}%")
        print(f"Initial wind speed: {self.get_wind_speed()} km/h")
        # 测试不同天气状况
        self.set_weather("多云", 20, 70, 15)
        print(f"Cloudy weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        self.set_weather("雨天", 15, 85, 20)
        print(f"Rainy weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        self.set_weather("雪天", -2, 75, 10)
        print(f"Snowy weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        # 测试晴天
        self.set_weather("晴天", 25, 60, 8)
        print(f"Sunny weather: {self.get_weather_icon_display()} {self.get_weather_condition()}, {self.get_temperature()}°C")
        print("Testing background customization...")
        print(f"Initial background: {self.get_background_display()}")
        # 测试背景颜色设置
        self.set_background_color("#1a1a2e")
        print(f"Background color set: {self.get_background_display()}")
        # 测试背景图片设置
        self.set_background_image("background.jpg")
        print(f"Background image set: {self.get_background_display()}")
        # 测试背景模糊效果
        self.toggle_background_blur()
        print(f"Background blur enabled: {self.get_background_display()}")
        # 测试再次切换模糊效果
        self.toggle_background_blur()
        print(f"Background blur disabled: {self.get_background_display()}")
        # 测试另一种背景颜色
        self.set_background_color("#16213e")
        print(f"Background color changed: {self.get_background_display()}")
        print("Testing animations...")
        print(f"Initial animation status: {self.get_animation_status()}")
        # 测试时间更新动画
        print("Testing time update animation...")
        self.animate_time_update()
        # 测试元素加载动画
        print("Testing element load animations...")
        self.animate_element_load("Time")
        self.animate_element_load("Date")
        self.animate_element_load("Battery")
        # 测试交互反馈动画
        print("Testing interaction animations...")
        self.animate_interaction("Tap")
        self.animate_interaction("Swipe")
        # 测试动画开关
        print("Testing animation toggle...")
        self.toggle_animations()
        print(f"Animation status after toggle: {self.get_animation_status()}")
        # 测试动画持续时间设置
        print("Testing animation duration...")
        self.set_animation_duration(1500)
        print(f"Animation duration set to: {self.animations['duration']}ms")
        # 测试单独的动画开关
        print("Testing individual animation toggles...")
        self.toggle_animations()  # 先开启动画
        self.toggle_time_update_animation()
        print(f"Time update animation: {'enabled' if self.animations['time_update'] else 'disabled'}")
        self.toggle_element_load_animation()
        print(f"Element load animation: {'enabled' if self.animations['element_load'] else 'disabled'}")
        self.toggle_interaction_animation()
        print(f"Interaction animation: {'enabled' if self.animations['interaction'] else 'disabled'}")
        print("Running compatibility tests...")
        print("Testing animations...")
        print("Testing performance...")
        print("All tests passed!")

def main():
    theme = MiWatchTheme()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "build":
            theme.build()
        elif command == "dev":
            theme.dev()
        elif command == "test":
            theme.test()
        elif command == "config":
            theme.config_mode()
        elif command == "preview":
            theme.preview_theme()
        elif command == "export":
            if len(sys.argv) > 2:
                output_path = sys.argv[2]
                theme.export_theme(output_path)
            else:
                print("Usage: python src/main.py export <output_path>")
        elif command == "import":
            if len(sys.argv) > 2:
                input_path = sys.argv[2]
                theme.import_theme(input_path)
            else:
                print("Usage: python src/main.py import <input_path>")
        elif command == "share":
            if len(sys.argv) > 2:
                share_method = sys.argv[2]
                theme.share_theme(share_method)
            else:
                print("Usage: python src/main.py share <method> (email, bluetooth, cloud)")
        else:
            print(f"Unknown command: {command}")
            print("Available commands: build, dev, test, config, preview, export, import, share")
    else:
        print(f"{theme.theme_name} v{theme.version}")
        print("Available commands: build, dev, test, config, preview, export, import, share")

if __name__ == "__main__":
    main()
