import os
import sys
import threading
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from groq import Groq

# Ép mã hóa UTF-8 cho toàn bộ luồng xuất chuẩn để tránh lỗi font/ASCII
if sys.stdout.encoding.lower() != 'utf-8':
  sys.reconfigure(encoding='utf-8')

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class PseudoReaderApp(ctk.CTk):

  def __init__(self):
    super().__init__()
    self.title("Pseudo-Reader")
    self.geometry("1050x680")
    self.minsize(900, 600)

    self.groq_api_key = os.environ.get("GROQ_API_KEY", "")
    self.client = Groq(api_key=self.groq_api_key) if self.groq_api_key else None

    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)

    self._init_sidebar()
    self._init_main()
    self.switch_view("dashboard")

  def _init_sidebar(self):
    self.sidebar = ctk.CTkFrame(
        self, width=240, corner_radius=0, fg_color=("#1a1a1a", "#121212")
    )
    self.sidebar.grid(row=0, column=0, sticky="nsew")
    self.sidebar.grid_rowconfigure(5, weight=1)

    logo = ctk.CTkLabel(
        self.sidebar,
        text="⚡ PSEUDO-READER",
        font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
        text_color="#3b82f6",
    )
    logo.grid(row=0, column=0, padx=20, pady=(30, 20), sticky="w")

    sub = ctk.CTkLabel(
        self.sidebar,
        text="Open Source Edition",
        font=ctk.CTkFont(family="Segoe UI", size=11),
        text_color="#888888",
    )
    sub.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

    self.b_dash = self._make_nav("Overview", "dashboard", 2)
    self.b_read = self._make_nav("Analyzation", "reader", 3)
    self.b_sett = self._make_nav("Settings", "settings", 4)

    footer = ctk.CTkLabel(
        self.sidebar,
        text="v1.0.0\ncoded by hunggmd_",
        font=ctk.CTkFont(size=10),
        text_color="#555555",
    )
    footer.grid(row=6, column=0, padx=20, pady=20, sticky="sw")

  def _make_nav(self, text, name, row):
    btn = ctk.CTkButton(
        self.sidebar,
        text=text,
        anchor="w",
        fg_color="transparent",
        text_color=("#c0c0c0", "#d0d0d0"),
        hover_color=("#2b2b2b", "#1f2937"),
        font=ctk.CTkFont(size=13, weight="bold"),
        corner_radius=8,
        height=40,
        command=lambda: self.switch_view(name),
    )
    btn.grid(row=row, column=0, padx=12, pady=4, sticky="ew")
    return btn

  def _init_main(self):
    self.main_frame = ctk.CTkFrame(
        self, corner_radius=0, fg_color=("#f3f4f6", "#0f172a")
    )
    self.main_frame.grid(row=0, column=1, sticky="nsew")
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_rowconfigure(0, weight=1)

    self.views = {
        "dashboard": self._build_dashboard(),
        "reader": self._build_reader(),
        "settings": self._build_settings(),
    }

    for f in self.views.values():
      f.grid(row=0, column=0, sticky="nsew")

  def switch_view(self, name):
    for n, b in [
        ("dashboard", self.b_dash),
        ("reader", self.b_read),
        ("settings", self.b_sett),
    ]:
      if n == name:
        b.configure(fg_color=("#2563eb", "#1d4ed8"), text_color="#ffffff")
      else:
        b.configure(fg_color="transparent", text_color=("#c0c0c0", "#d0d0d0"))
    self.views[name].tkraise()

  def _build_dashboard(self):
    f = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    f.grid_columnconfigure(0, weight=1)

    t = ctk.CTkLabel(
        f,
        text="Pseudo-Reader",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color=("#111827", "#f8fafc"),
    )
    t.pack(anchor="w", padx=40, pady=(40, 10))

    d = ctk.CTkLabel(
        f,
        text=(
            "Fast text-to-code analyzer using Qwen 3.8 27B Engine.\nChoose"
            " 'Analyzation' from the navigation panel to start."
        ),
        font=ctk.CTkFont(size=14),
        text_color=("#4b5563", "#94a3b8"),
        justify="left",
    )
    d.pack(anchor="w", padx=40, pady=(0, 30))

    card = ctk.CTkFrame(f, fg_color=("#ffffff", "#1e293b"), corner_radius=12)
    card.pack(fill="x", padx=40, pady=10)

    ct = ctk.CTkLabel(
        card,
        text="System State",
        font=ctk.CTkFont(size=16, weight="bold"),
        text_color=("#2563eb", "#60a5fa"),
    )
    ct.pack(anchor="w", padx=20, pady=(20, 10))

    self.lbl_status = ctk.CTkLabel(
        card,
        text=(
            "• API Status: "
            + ("Connected" if self.groq_api_key else "Not configured")
        ),
        font=ctk.CTkFont(size=13),
        text_color=("#374151", "#cbd5e1"),
    )
    self.lbl_status.pack(anchor="w", padx=20, pady=5)

    m = ctk.CTkLabel(
        card,
        text="• Engine: qwen/qwen3.8-27b",
        font=ctk.CTkFont(size=13),
        text_color=("#374151", "#cbd5e1"),
    )
    m.pack(anchor="w", padx=20, pady=(5, 20))

    return f

  def _build_reader(self):
    f = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    f.grid_columnconfigure(0, weight=1)
    f.grid_rowconfigure(2, weight=1)

    t = ctk.CTkLabel(
        f,
        text="Analyze",
        font=ctk.CTkFont(size=22, weight="bold"),
        text_color=("#111827", "#f8fafc"),
    )
    t.grid(row=0, column=0, sticky="w", padx=40, pady=(30, 10))

    in_f = ctk.CTkFrame(f, fg_color=("#ffffff", "#1e293b"), corner_radius=12)
    in_f.grid(row=1, column=0, sticky="ew", padx=40, pady=10)
    in_f.grid_columnconfigure(0, weight=1)

    li = ctk.CTkLabel(
        in_f,
        text="User Input:",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color=("#374151", "#e2e8f0"),
    )
    li.grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))

    self.t_in = ctk.CTkTextbox(
        in_f,
        height=100,
        corner_radius=8,
        font=ctk.CTkFont(size=13),
        border_width=1,
        border_color=("#d1d5db", "#475569"),
    )
    self.t_in.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))

    btn = ctk.CTkButton(
        in_f,
        text="Execute",
        font=ctk.CTkFont(size=14, weight="bold"),
        fg_color="#2563eb",
        hover_color="#1d4ed8",
        height=40,
        corner_radius=8,
        command=self.run_process,
    )
    btn.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="e")

    out_f = ctk.CTkFrame(f, fg_color=("#ffffff", "#1e293b"), corner_radius=12)
    out_f.grid(row=2, column=0, sticky="nsew", padx=40, pady=(10, 30))
    out_f.grid_columnconfigure(0, weight=1)
    out_f.grid_rowconfigure(1, weight=1)

    lo = ctk.CTkLabel(
        out_f,
        text="Processed result:",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color=("#374151", "#e2e8f0"),
    )
    lo.grid(row=0, column=0, sticky="w", padx=40, pady=(15, 5))

    self.t_out = ctk.CTkTextbox(
        out_f,
        corner_radius=8,
        font=ctk.CTkFont(size=13),
        border_width=1,
        border_color=("#d1d5db", "#475569"),
    )
    self.t_out.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
    self.t_out.insert("0.0", "Qwen 3.8 27B Engine is ready...")

    return f

  def _build_settings(self):
    f = ctk.CTkFrame(self.main_frame, fg_color="transparent")
    f.grid_columnconfigure(0, weight=1)

    t = ctk.CTkLabel(
        f,
        text="API Configuration",
        font=ctk.CTkFont(size=22, weight="bold"),
        text_color=("#111827", "#f8fafc"),
    )
    t.grid(row=0, column=0, sticky="w", padx=40, pady=(30, 10))

    card = ctk.CTkFrame(f, fg_color=("#ffffff", "#1e293b"), corner_radius=12)
    card.grid(row=1, column=0, sticky="ew", padx=40, pady=10)
    card.grid_columnconfigure(0, weight=1)

    lk = ctk.CTkLabel(
        card,
        text="Groq API Key:",
        font=ctk.CTkFont(size=13, weight="bold"),
        text_color=("#374151", "#e2e8f0"),
    )
    lk.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))

    self.e_key = ctk.CTkEntry(
        card,
        show="*",
        placeholder_text="gsk_...",
        height=38,
        corner_radius=8,
        font=ctk.CTkFont(size=13),
    )
    self.e_key.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 15))
    if self.groq_api_key:
      self.e_key.insert(0, self.groq_api_key)

    bs = ctk.CTkButton(
        card,
        text="Save API Key",
        font=ctk.CTkFont(size=13, weight="bold"),
        fg_color="#10b981",
        hover_color="#059669",
        height=36,
        corner_radius=8,
        command=self.save_key,
    )
    bs.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="e")

    return f

  def save_key(self):
    k = self.e_key.get().strip()
    if not k:
      messagebox.showerror("Error", "Please enter a valid API key!")
      return
    self.groq_api_key = k
    self.client = Groq(api_key=self.groq_api_key)
    self.lbl_status.configure(text="* API Status: Connected")
    messagebox.showinfo("Success", "API Saved!")

  def run_process(self):
    if not self.client:
      messagebox.showwarning("Warning", "Please consider enter your own API key!")
      self.switch_view("settings")
      return

    p = self.t_in.get("0.0", "end").strip()
    if not p:
      messagebox.showwarning("Warning", "Can't leave 'Input' blank.")
      return

    self.t_out.delete("0.0", "end")
    self.t_out.insert("0.0", "Processing...")
    threading.Thread(target=self._exec_api, args=(p,), daemon=True).start()

  def _exec_api(self, p):
    try:
      res = self.client.chat.completions.create(
          model="qwen/qwen3.8-27b",
          messages=[{"role": "user", "content": p}],
          temperature=0.7,
      )
      self.t_out.delete("0.0", "end")
      self.t_out.insert("0.0", res.choices[0].message.content)
    except Exception as e:
      self.t_out.delete("0.0", "end")
      self.t_out.insert("0.0", f"Execution Error: {str(e)}")


if __name__ == "__main__":
  app = PseudoReaderApp()
  app.mainloop()