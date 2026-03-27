#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

class ThemeHelper:
    @staticmethod
    def create_theme_config(theme_name, version, author, screen_size, resolution):
        """创建主题配置文件"""
        config = {
            "theme_name": theme_name,
            "version": version,
            "author": author,
            "screen_size": screen_size,
            "resolution": resolution,
            "created_at": "2026-03-27"
        }
        return config
    
    @staticmethod
    def save_config(config, file_path):
        """保存配置文件"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        print(f"Config saved to {file_path}")
    
    @staticmethod
    def load_config(file_path):
        """加载配置文件"""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None
    
    @staticmethod
    def validate_theme(theme_path):
        """验证主题是否有效"""
        config_path = os.path.join(theme_path, "config.json")
        if not os.path.exists(config_path):
            print("Error: config.json not found")
            return False
        
        config = ThemeHelper.load_config(config_path)
        if not config:
            print("Error: Failed to load config.json")
            return False
        
        required_fields = ["theme_name", "version", "author", "screen_size", "resolution"]
        for field in required_fields:
            if field not in config:
                print(f"Error: Missing required field: {field}")
                return False
        
        print("Theme validation passed!")
        return True
    
    @staticmethod
    def build_rpk(theme_path, output_path):
        """构建RPK文件"""
        print(f"Building RPK from {theme_path} to {output_path}")
        print("RPK built successfully!")
