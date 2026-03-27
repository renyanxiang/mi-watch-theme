#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Canvas:
    def __init__(self, width=466, height=466):
        self.width = width
        self.height = height
        self.elements = []
    
    def add_element(self, element):
        """添加元素"""
        self.elements.append(element)
    
    def clear(self):
        """清空画布"""
        self.elements = []
    
    def render(self):
        """渲染画布"""
        print(f"Rendering canvas: {self.width}x{self.height}")
        for element in self.elements:
            element.render()

class TextElement:
    def __init__(self, x, y, text, font_size=20, color="#FFFFFF"):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.color = color
    
    def render(self):
        """渲染文本元素"""
        print(f"Rendering text: '{self.text}' at ({self.x}, {self.y}) with size {self.font_size} and color {self.color}")

class ImageElement:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_path = image_path
    
    def render(self):
        """渲染图片元素"""
        print(f"Rendering image: {self.image_path} at ({self.x}, {self.y}) with size {self.width}x{self.height}")

class ShapeElement:
    def __init__(self, x, y, width, height, color="#FFFFFF", shape_type="rectangle"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.shape_type = shape_type
    
    def render(self):
        """渲染形状元素"""
        print(f"Rendering {self.shape_type}: at ({self.x}, {self.y}) with size {self.width}x{self.height} and color {self.color}")
