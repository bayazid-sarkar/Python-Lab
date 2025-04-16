import tkinter as tk
from tkinter import ttk, filedialog, colorchooser, messagebox
from PIL import Image, ImageTk, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import SolidFillColorMask
import os

class ModernQRDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title("QR-সাজাই")
        self.root.geometry("500x700")
        self.root.minsize(450, 600)
        
        # Initialize style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Theme setup
        self.dark_mode = False
        self.setup_themes()
        self.set_theme()
        
        # Style options
        self.style_options = {
            "Square": SquareModuleDrawer(),
            "Gapped": GappedSquareModuleDrawer(),
            "Circle": CircleModuleDrawer(),
            "Rounded": RoundedModuleDrawer(),
        }
        
        # Variables
        self.qr_text = tk.StringVar()
        self.qr_style = tk.StringVar(value="Square")
        self.foreground_color = (0, 0, 0)  # Black
        self.background_color = (255, 255, 255)  # White
        self.qr_size = tk.IntVar(value=250)
        self.logo_path = ""
        self.generated_qr = None
        self.last_update_id = None
        
        # Setup UI
        self.create_ui()
        self.setup_bindings()
    
    def setup_themes(self):
        self.themes = {
            "light": {
                "bg": "#ffffff",  # White background
                "surface": "#f5f5f5",  # Light gray surface
                "text": "#000000",  # Black text
                "primary": "#008000",  # Green for primary buttons
                "button_primary": "#008000",  # Green for primary buttons
                "button_secondary": "#FFA500",  # Orange for secondary buttons
                "button_danger": "#FF4500",  # Orange-red for remove actions
                "border": "#e0e0e0",  # Light gray border
                "highlight": "#f0f0f0",  # Very light gray for highlights
                "text_secondary": "#333333",  # Dark gray for secondary text
                "slider_trough": "#e0e0e0",  # Light gray for slider trough
                "slider_active": "#008000",  # Green for active slider
                "combobox_arrow": "#333333"  # Dark gray for combobox arrow
            },
            "dark": {
                "bg": "#121212",  # Very dark gray (almost black)
                "surface": "#1e1e1e",  # Dark gray surface
                "text": "#ffffff",  # White text
                "primary": "#4CAF50",  # Brighter green for primary buttons
                "button_primary": "#4CAF50",  # Brighter green for primary buttons
                "button_secondary": "#FF8C00",  # Darker orange for secondary buttons
                "button_danger": "#FF6347",  # Tomato red for remove actions
                "border": "#333333",  # Dark gray border
                "highlight": "#2a2a2a",  # Slightly lighter than bg
                "text_secondary": "#cccccc",  # Light gray for secondary text
                "slider_trough": "#333333",  # Dark gray for slider trough
                "slider_active": "#4CAF50",  # Green for active slider
                "combobox_arrow": "#ffffff"  # White for combobox arrow
            }
        }
    
    def set_theme(self):
        theme = self.themes["dark" if self.dark_mode else "light"]
        
        # Update theme colors
        self.bg_color = theme["bg"]
        self.surface_color = theme["surface"]
        self.text_color = theme["text"]
        self.primary_color = theme["primary"]
        self.button_primary = theme["button_primary"]
        self.button_secondary = theme["button_secondary"]
        self.button_danger = theme["button_danger"]
        self.border_color = theme["border"]
        self.highlight_color = theme["highlight"]
        self.text_secondary = theme["text_secondary"]
        self.slider_trough = theme["slider_trough"]
        self.slider_active = theme["slider_active"]
        self.combobox_arrow = theme["combobox_arrow"]
        
        # Configure styles
        self.style.configure(".", background=self.bg_color, foreground=self.text_color)
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color)
        
        # Primary buttons (green) - More prominent hover effects
        self.style.configure("Primary.TButton", 
                           background=self.button_primary,
                           foreground="white",
                           borderwidth=0,
                           focusthickness=0,
                           focuscolor='none',
                           font=('Segoe UI', 9, 'bold'),
                           padding=8,
                           relief="flat",
                           bordercolor=self.border_color)
        self.style.map("Primary.TButton",
                      background=[('active', self.darken_color(self.button_primary, 40)), 
                                 ('pressed', self.darken_color(self.button_primary, 60))],
                      relief=[('active', 'sunken'), ('pressed', 'sunken')])
        
        # Secondary buttons (orange) - More prominent hover effects
        self.style.configure("Secondary.TButton", 
                           background=self.button_secondary,
                           foreground="white",
                           borderwidth=0,
                           focusthickness=0,
                           focuscolor='none',
                           font=('Segoe UI', 9, 'bold'),
                           padding=8,
                           relief="flat")
        self.style.map("Secondary.TButton",
                      background=[('active', self.darken_color(self.button_secondary, 40)), 
                                 ('pressed', self.darken_color(self.button_secondary, 60))],
                      relief=[('active', 'sunken'), ('pressed', 'sunken')])
        
        # Danger buttons (orange-red) - More prominent hover effects
        self.style.configure("Danger.TButton", 
                           background=self.button_danger,
                           foreground="white",
                           borderwidth=0,
                           focusthickness=0,
                           focuscolor='none',
                           font=('Segoe UI', 9, 'bold'),
                           padding=8,
                           relief="flat")
        self.style.map("Danger.TButton",
                      background=[('active', self.darken_color(self.button_danger, 40)), 
                                 ('pressed', self.darken_color(self.button_danger, 60))],
                      relief=[('active', 'sunken'), ('pressed', 'sunken')])
        
        # Modern Combobox styling
        self.style.configure("Modern.TCombobox", 
                           fieldbackground=self.surface_color,
                           background=self.surface_color,
                           foreground=self.text_color,
                           selectbackground=self.button_primary,
                           selectforeground="white",
                           font=('Segoe UI', 10),
                           padding=6,
                           relief="flat",
                           bordercolor=self.border_color,
                           lightcolor=self.border_color,
                           darkcolor=self.border_color,
                           arrowsize=12,
                           arrowcolor=self.combobox_arrow)
        self.style.map("Modern.TCombobox",
                      fieldbackground=[('readonly', self.surface_color)],
                      background=[('readonly', self.surface_color)],
                      bordercolor=[('active', self.button_primary),
                                  ('focus', self.button_primary)],
                      lightcolor=[('active', self.button_primary),
                                 ('focus', self.button_primary)],
                      darkcolor=[('active', self.button_primary),
                                ('focus', self.button_primary)])
        
        # Modern Scale (Slider) styling
        self.style.configure("Modern.Horizontal.TScale",
                           background=self.bg_color,
                           troughcolor=self.slider_trough,
                           bordercolor=self.border_color,
                           lightcolor=self.border_color,
                           darkcolor=self.border_color,
                           troughrelief="flat",
                           sliderrelief="raised",
                           sliderthickness=14)
        self.style.map("Modern.Horizontal.TScale",
                      slidercolor=[('active', self.slider_active)],
                      troughcolor=[('active', self.slider_trough)])
        
        # Toggle button styling with more prominent hover
        self.style.configure("Toggle.TButton", 
                           background=self.highlight_color,
                           foreground=self.text_color,
                           font=('Segoe UI', 10, 'bold'),
                           padding=6)
        self.style.map("Toggle.TButton",
                      background=[('active', self.darken_color(self.highlight_color, 20)),
                                 ('pressed', self.darken_color(self.highlight_color, 40))])
        
        # Update all widgets
        self.root.configure(bg=self.bg_color)
        if hasattr(self, 'main_frame'):
            self.main_frame.configure(style="TFrame")
        if hasattr(self, 'input_frame'):
            self.input_frame.configure(style="TFrame")
        if hasattr(self, 'preview_frame'):
            self.preview_frame.configure(style="TFrame")
            self.preview_frame.configure(highlightbackground=self.border_color)
        
        # Update toggle button
        if hasattr(self, 'theme_toggle'):
            self.theme_toggle.configure(text="☀️" if self.dark_mode else "🌙",
                                      style="Toggle.TButton")
        
        # Update other buttons
        if hasattr(self, 'fg_btn'):
            self.fg_btn.configure(style="Secondary.TButton")
        if hasattr(self, 'bg_btn'):
            self.bg_btn.configure(style="Secondary.TButton")
        if hasattr(self, 'logo_add_btn'):
            self.logo_add_btn.configure(style="Secondary.TButton")
        if hasattr(self, 'logo_remove_btn'):
            self.logo_remove_btn.configure(style="Danger.TButton")
        if hasattr(self, 'save_btn'):
            self.save_btn.configure(style="Primary.TButton")
    
    def darken_color(self, color, amount=10):
        """Darken a hex color by a certain amount"""
        if isinstance(color, str) and color.startswith('#'):
            rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
            return f'#{max(0, rgb[0]-amount):02x}{max(0, rgb[1]-amount):02x}{max(0, rgb[2]-amount):02x}'
        return color
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
    
    def setup_bindings(self):
        self.qr_text.trace_add("write", lambda *args: self.schedule_preview_update())
        self.qr_style.trace_add("write", lambda *args: self.schedule_preview_update())
        self.qr_size.trace_add("write", lambda *args: self.schedule_preview_update())
    
    def schedule_preview_update(self):
        if self.last_update_id:
            self.root.after_cancel(self.last_update_id)
        self.last_update_id = self.root.after(500, self.update_live_preview)
    
    def create_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding=(15, 10))
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with theme toggle
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Title with green color
        title = ttk.Label(header_frame, text="QR-সাজাই", 
                         font=("Segoe UI", 18, "bold"),
                         foreground=self.button_primary)
        title.pack(side=tk.LEFT)
        
        # Theme toggle button
        self.theme_toggle = ttk.Button(header_frame, text="☀️" if self.dark_mode else "🌙",
                                     command=self.toggle_theme, style="Toggle.TButton")
        self.theme_toggle.pack(side=tk.RIGHT)
        
        # Input Section
        self.input_frame = ttk.Frame(self.main_frame, padding=10, relief=tk.RIDGE, borderwidth=1)
        self.input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.input_frame, text="Enter URL, TEXT or Link", font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 5))
        self.content_entry = ttk.Entry(self.input_frame, textvariable=self.qr_text, 
                                     font=("Segoe UI", 10))
        self.content_entry.pack(fill=tk.X, pady=5)
        
        # Style and Colors
        style_color_frame = ttk.Frame(self.main_frame)
        style_color_frame.pack(fill=tk.X, pady=5)
        
        # Modern Style dropdown
        ttk.Label(style_color_frame, text="QR STYLE:", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w", padx=(5, 0))
        style_menu = ttk.Combobox(style_color_frame, textvariable=self.qr_style, 
                                values=list(self.style_options.keys()), 
                                state="readonly", width=12, font=("Segoe UI", 9),
                                style="Modern.TCombobox")
        style_menu.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        
        # Configure popup menu for combobox
        style_menu.bind("<<ComboboxSelected>>", lambda e: self.root.focus())
        
        # Color buttons (orange)
        color_frame = ttk.Frame(style_color_frame)
        color_frame.grid(row=0, column=1, rowspan=2, sticky="e", padx=5)
        
        self.fg_btn = ttk.Button(color_frame, text="Foreground", command=self.choose_foreground_color,
                               style="Primary.TButton")
        self.fg_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.bg_btn = ttk.Button(color_frame, text="Background", command=self.choose_background_color,
                               style="Secondary.TButton")
        self.bg_btn.pack(side=tk.LEFT)
        
        # Size and Logo
        size_logo_frame = ttk.Frame(self.main_frame)
        size_logo_frame.pack(fill=tk.X, pady=5)
        
        # Modern Size slider
        ttk.Label(size_logo_frame, text=f"ADJUST SIZE", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w", padx=(5, 0))
        size_slider = ttk.Scale(size_logo_frame, from_=150, to=500, variable=self.qr_size, 
                              command=self.on_size_change, length=180,
                              style="Modern.Horizontal.TScale")
        size_slider.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        
        # Custom slider styling (additional tweaks)
        self.style.configure("Modern.Horizontal.TScale",
                           slidercolor=self.slider_active,
                           troughcolor=self.slider_trough)
        
        # Logo buttons (orange for add, orange-red for remove)
        logo_frame = ttk.Frame(size_logo_frame)
        logo_frame.grid(row=0, column=1, rowspan=2, sticky="e", padx=5)
        
        self.logo_add_btn = ttk.Button(logo_frame, text="Add Logo", command=self.upload_logo,
                                     style="Primary.TButton")
        self.logo_add_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.logo_remove_btn = ttk.Button(logo_frame, text="Remove Logo", command=self.clear_logo,
                                        style="Danger.TButton")
        self.logo_remove_btn.pack(side=tk.LEFT)
        
        # Preview area
        self.preview_frame = ttk.Frame(self.main_frame, relief=tk.SOLID, borderwidth=1)
        self.preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.qr_preview_label = ttk.Label(self.preview_frame, text="Your QR code will appear here",
                                        font=("Segoe UI", 10), anchor="center")
        self.qr_preview_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Save button (green)
        self.save_btn = ttk.Button(self.main_frame, text="SAVE QR CODE", command=self.save_qr,
                                 style="Primary.TButton")
        self.save_btn.pack(fill=tk.X, pady=5)
        
        # Status bar
        self.status_label = ttk.Label(self.main_frame, text="Ready", font=("Segoe UI", 8), anchor="w")
        self.status_label.pack(fill=tk.X, pady=(5, 0))
        
        # Initial preview update
        self.update_live_preview()
    
    def on_size_change(self, value):
        self.qr_size.set(int(float(value)))
        self.schedule_preview_update()
    
    def choose_foreground_color(self):
        color = colorchooser.askcolor(title="Choose Foreground Color", initialcolor="#000000")
        if color[0]:
            self.foreground_color = tuple(map(int, color[0]))
            self.schedule_preview_update()
    
    def choose_background_color(self):
        color = colorchooser.askcolor(title="Choose Background Color", initialcolor="#FFFFFF")
        if color[0]:
            self.background_color = tuple(map(int, color[0]))
            self.schedule_preview_update()
    
    def upload_logo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.logo_path = file_path
            self.schedule_preview_update()
    
    def clear_logo(self):
        self.logo_path = ""
        self.schedule_preview_update()
    
    def update_live_preview(self):
        if not self.qr_text.get():
            self.qr_preview_label.config(text="Your QR code will appear here", image=None)
            return
            
        try:
            self.generate_qr(update_preview=True)
            self.status_label.config(text="Preview updated")
        except Exception as e:
            self.status_label.config(text=f"Preview error: {str(e)}")
    
    def generate_qr(self, update_preview=True):
        text = self.qr_text.get()
        if not text:
            if update_preview:
                self.qr_preview_label.config(text="Please enter content first", image=None)
            return
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            selected_style = self.style_options[self.qr_style.get()]
            qr_img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=selected_style,
                color_mask=SolidFillColorMask(
                    front_color=self.foreground_color,
                    back_color=self.background_color
                )
            )
            
            if self.logo_path:
                qr_img = self.add_logo(qr_img)
            
            target_size = self.qr_size.get()
            qr_img = qr_img.resize((target_size, target_size), Image.LANCZOS)
            
            self.generated_qr = qr_img
            
            if update_preview:
                self.update_qr_preview()
            
        except Exception as e:
            if update_preview:
                self.qr_preview_label.config(text=f"Error: {str(e)}", image=None)
            raise
    
    def add_logo(self, qr_img):
        try:
            logo = Image.open(self.logo_path).convert("RGBA")
            qr_width, qr_height = qr_img.size
            logo_size = min(qr_width, qr_height) // 4
            logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
            
            mask = Image.new("L", (logo_size, logo_size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, logo_size, logo_size), fill=255)
            
            logo.putalpha(mask)
            position = ((qr_width - logo.size[0]) // 2, (qr_height - logo.size[1]) // 2)
            
            logo_layer = Image.new("RGBA", qr_img.size, (0, 0, 0, 0))
            logo_layer.paste(logo, position, mask=logo)
            
            return Image.alpha_composite(qr_img.convert("RGBA"), logo_layer).convert("RGB")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add logo: {str(e)}")
            return qr_img
    
    def update_qr_preview(self):
        if not self.generated_qr:
            return
            
        available_width = self.preview_frame.winfo_width() - 20
        available_height = self.preview_frame.winfo_height() - 20
        preview_size = min(available_width, available_height, 300)
        
        img = self.generated_qr.copy()
        img.thumbnail((preview_size, preview_size), Image.LANCZOS)
        
        photo = ImageTk.PhotoImage(img)
        self.qr_preview_label.config(image=photo, text="")
        self.qr_preview_label.image = photo
    
    def save_qr(self):
        if not self.generated_qr:
            messagebox.showerror("Error", "No QR code generated to save")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All Files", "*.*")],
            initialfile="qr_code.png"
        )
        
        if file_path:
            try:
                self.generated_qr.save(file_path)
                messagebox.showinfo("Success", f"QR code saved to:\n{file_path}")
                self.status_label.config(text=f"Saved: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code: {str(e)}")
                self.status_label.config(text="Save failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernQRDesigner(root)
    root.mainloop()