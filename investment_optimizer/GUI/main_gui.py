import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if project_root not in sys.path:
    sys.path.append(project_root)

from Algorithms.branch_bound import branch_and_bound
from Algorithms.dynamic_programming import dynamic_programming
from Algorithms.genetic_algorithm import genetic_algorithm


class InvestmentOptimizerGUI:

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TNotebook", background="#0f1115", borderwidth=0, highlightthickness=0)
        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 10, "bold"), padding=(25, 8),
            background="#171a21", foreground="#94a3b8", borderwidth=0, focuscolor=""
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", "#c5a059")], 
            foreground=[("selected", "#0f1115")]
        )
        style.configure("TSeparator", background="#262a35")
        
        # Style for the scrollbar to match dark theme better
        style.configure(
            "Vertical.TScrollbar",
            background="#171a21", troughcolor="#0f1115", 
            bordercolor="#0f1115", arrowcolor="#c5a059"
        )

    def __init__(self, root):
        self.root = root
        self.root.title("Investment Optimization System")
        self.root.geometry("1400x920")
        self.root.configure(bg="#0f1115")
        self.root.minsize(1100, 750)

        self.configure_styles()
        
        # 1. SETUP SCROLLABLE AREA
        self.setup_scrollable_area()
        
        # 2. CREATE WIDGETS INSIDE SCROLLABLE AREA
        self.create_widgets()
        
        self.create_algorithm_cards(self.tab1)
        self.create_algorithm_cards(self.tab2)
        self.create_algorithm_cards(self.tab3)

    # =================================
    # SCROLLABLE CANVAS SETUP
    # =================================
    def setup_scrollable_area(self):
        # Container utama
        self.main_container = tk.Frame(self.root, bg="#0f1115")
        self.main_container.pack(fill="both", expand=True)

        # Canvas untuk scrolling
        self.canvas = tk.Canvas(self.main_container, bg="#0f1115", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=self.canvas.yview, style="Vertical.TScrollbar")
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame yang akan menampung seluruh isi UI
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0f1115")
        
        # Masukkan frame ke dalam canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Binding untuk update area scroll saat isi berubah
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Binding agar lebar frame mengikuti lebar canvas
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width)
        )

        # Fitur scroll dengan roda mouse (Mousewheel)
        self.root.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # =================================
    # UI COMPONENTS
    # =================================
    def create_widgets(self):
        # Semua elemen sekarang dipasang ke self.scrollable_frame, BUKAN self.root

        # =============================
        # HEADER
        # =============================
        header_frame = tk.Frame(self.scrollable_frame, bg="#0f1115")
        header_frame.pack(fill="x", padx=30, pady=(25, 15))

        title_label = tk.Label(
            header_frame,
            text="INVESTMENT OPTIMIZATION SYSTEM",
            font=("Georgia", 22, "bold") if "Georgia" in tkfont.families() else ("Segoe UI", 20, "bold"),
            fg="#c5a059", bg="#0f1115"
        )
        title_label.pack(anchor="w")

        subtitle_label = tk.Label(
            header_frame,
            text="Institutional-Grade Comparative Analysis Matrix // Wealth Management Division",
            font=("Segoe UI", 9, "bold"),
            fg="#4b5262", bg="#0f1115"
        )
        subtitle_label.pack(anchor="w", pady=(4, 0))

        # =============================
        # TOP CONFIG PANEL
        # =============================
        top_frame = tk.Frame(self.scrollable_frame, bg="#0f1115")
        top_frame.pack(fill="x", padx=30, pady=10)

        # 1. Input Parameter Card
        input_card = tk.Frame(top_frame, bg="#171a21", bd=1, highlightbackground="#262a35", highlightthickness=1)
        input_card.pack(side="left", fill="both", expand=True, padx=(0, 15))

        input_title = tk.Label(input_card, text="PORTFOLIO PARAMETERS", font=("Segoe UI", 10, "bold"), fg="#c5a059", bg="#171a21")
        input_title.pack(anchor="w", padx=20, pady=(15, 5))

        input_content = tk.Frame(input_card, bg="#171a21")
        input_content.pack(fill="both", padx=20, pady=(0, 15))

        tk.Label(input_content, text="Initial Capital / Modal Awal (Rp)", bg="#171a21", fg="#94a3b8", font=("Segoe UI", 9)).pack(anchor="w")
        
        self.modal_entry = tk.Entry(
            input_content, font=("Consolas", 12), bg="#0f1115", fg="#f3f4f6",
            insertbackground="white", bd=0, highlightbackground="#262a35", highlightthickness=1, width=25
        )
        self.modal_entry.pack(pady=(5, 12), fill="x", ipady=5)
        self.modal_entry.insert(0, "100000000")

        self.run_button = tk.Button(
            input_content, text="EXECUTE OPTIMIZATION", bg="#c5a059", fg="#0f1115",
            font=("Segoe UI", 10, "bold"), relief="flat", activebackground="#d4af37", activeforeground="#0f1115",
            cursor="hand2", command=self.run_optimization
        )
        self.run_button.pack(fill="x", ipady=4)
        
        self.run_button.bind("<Enter>", lambda e: self.run_button.config(bg="#d4af37"))
        self.run_button.bind("<Leave>", lambda e: self.run_button.config(bg="#c5a059"))

        # 2. Risk Limit Scenario Card
        risk_card = tk.Frame(top_frame, bg="#171a21", bd=1, highlightbackground="#262a35", highlightthickness=1)
        risk_card.pack(side="left", fill="both", expand=True)

        risk_title = tk.Label(risk_card, text="RISK TOLERANCE TRANCHES", font=("Segoe UI", 10, "bold"), fg="#c5a059", bg="#171a21")
        risk_title.pack(anchor="w", padx=20, pady=(15, 10))

        risk_content = tk.Frame(risk_card, bg="#171a21")
        risk_content.pack(fill="both", padx=20, pady=(0, 15))

        scenarios_info = [
            ("TRANCHE 1", "Risk Limit 3.5 — Capital Preservation / Conservative"),
            ("TRANCHE 2", "Risk Limit 4.0 — Balanced Growth / Moderate"),
            ("TRANCHE 3", "Risk Limit 4.5 — Alpha Generation / Aggressive")
        ]
        for title_scen, desc_scen in scenarios_info:
            scen_row = tk.Frame(risk_content, bg="#171a21")
            scen_row.pack(anchor="w", pady=4)
            tk.Label(scen_row, text=title_scen, bg="#171a21", fg="#c5a059", font=("Segoe UI", 9, "bold"), width=12, anchor="w").pack(side="left")
            tk.Label(scen_row, text=desc_scen, bg="#171a21", fg="#6b7280", font=("Segoe UI", 9)).pack(side="left", padx=10)

        # =============================
        # NOTEBOOK / TABS
        # =============================
        self.notebook = ttk.Notebook(self.scrollable_frame)
        self.notebook.pack(fill="both", expand=True, padx=30, pady=(20, 25))

        self.tab1 = tk.Frame(self.notebook, bg="#0f1115")
        self.tab2 = tk.Frame(self.notebook, bg="#0f1115")
        self.tab3 = tk.Frame(self.notebook, bg="#0f1115")

        self.notebook.add(self.tab1, text="  TRANCHE 1 (3.5)  ")
        self.notebook.add(self.tab2, text="  TRANCHE 2 (4.0)  ")
        self.notebook.add(self.tab3, text="  TRANCHE 3 (4.5)  ")

    def create_algorithm_cards(self, parent):
        container = tk.Frame(parent, bg="#0f1115")
        container.pack(fill="both", expand=True, pady=(15, 30)) # Extra padding bottom for scrolling

        for i in range(3):
            container.grid_columnconfigure(i, weight=1, uniform="equal")
        container.grid_rowconfigure(0, weight=1)

        cards = ["Branch and Bound", "Dynamic Programming", "Genetic Algorithm"]

        for index, title in enumerate(cards):
            card_frame = tk.Frame(container, bg="#171a21", bd=0, highlightbackground="#262a35", highlightthickness=1)
            card_frame.grid(row=0, column=index, sticky="nsew", padx=8, pady=5)

            top_bar = tk.Frame(card_frame, bg="#c5a059", height=2)
            top_bar.pack(fill="x")

            card_title = tk.Label(card_frame, text=title.upper(), font=("Segoe UI", 11, "bold"), fg="#f3f4f6", bg="#171a21")
            card_title.pack(anchor="w", padx=15, pady=(12, 10))

            content = tk.Frame(card_frame, bg="#171a21")
            content.pack(fill="both", expand=True, padx=15, pady=(0, 15))

            # --- STATISTICS ---
            tk.Label(content, text="ANALYSIS METRICS", bg="#171a21", fg="#c5a059", font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(5, 2))
            
            total_label = tk.Label(content, text="Total Combinations : -", bg="#171a21", fg="#94a3b8", font=("Segoe UI", 10))
            total_label.pack(anchor="w", padx=5)
            
            valid_label = tk.Label(content, text="Feasible Nodes : -", bg="#171a21", fg="#94a3b8", font=("Segoe UI", 10))
            valid_label.pack(anchor="w", padx=5)
            
            invalid_label = tk.Label(content, text="Pruned / Infeasible : -", bg="#171a21", fg="#94a3b8", font=("Segoe UI", 10))
            invalid_label.pack(anchor="w", padx=5)

            ttk.Separator(content, orient="horizontal").pack(fill="x", pady=12)

            # --- TOP 3 SOLUTIONS ---
            tk.Label(content, text="TOP 3 ALLOCATIONS", bg="#171a21", fg="#c5a059", font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(0, 2))
            
            top1 = tk.Label(content, text="#1 -", bg="#171a21", fg="#e2e8f0", font=("Consolas", 10))
            top1.pack(anchor="w", padx=5, pady=1)
            top2 = tk.Label(content, text="#2 -", bg="#171a21", fg="#cbd5e1", font=("Consolas", 10))
            top2.pack(anchor="w", padx=5, pady=1)
            top3 = tk.Label(content, text="#3 -", bg="#171a21", fg="#94a3b8", font=("Consolas", 10))
            top3.pack(anchor="w", padx=5, pady=1)

            ttk.Separator(content, orient="horizontal").pack(fill="x", pady=12)

            # --- BEST SOLUTION CONTAINER ---
            tk.Label(content, text="OPTIMAL TARGET ALLOCATION", bg="#171a21", fg="#c5a059", font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(0, 4))
            
            best_box = tk.Frame(content, bg="#0f1115", bd=1, highlightbackground="#262a35", highlightthickness=1)
            best_box.pack(fill="x", pady=2, ipady=10) # Menambah padding vertikal (ipady) agar lega

            best_label = tk.Label(
                best_box, 
                text="-\n-", 
                bg="#0f1115", fg="#f3f4f6", font=("Segoe UI", 10, "bold"), justify="left"
            )
            best_label.pack(anchor="w", padx=10, pady=2)

            # --- RUNTIME FOOTER ---
            # Mengganti dari side="bottom" ke urutan normal
            runtime_frame = tk.Frame(content, bg="#1f232e")
            runtime_frame.pack(fill="x", pady=(15, 0), ipady=4)
            
            runtime_label = tk.Label(
                runtime_frame, text="  System Ready", bg="#1f232e", fg="#94a3b8", font=("Segoe UI", 9)
            )
            runtime_label.pack(side="left", padx=10)

            if not hasattr(self, "algorithm_widgets"):
                self.algorithm_widgets = {}
            if parent not in self.algorithm_widgets:
                self.algorithm_widgets[parent] = {}

            self.algorithm_widgets[parent][title] = {
                "total": total_label,
                "valid": valid_label,
                "invalid": invalid_label,
                "top1": top1,
                "top2": top2,
                "top3": top3,
                "best": best_label,
                "runtime": runtime_label
            }

    def update_algorithm_card(self, parent, algorithm_name, result):
        widgets = self.algorithm_widgets[parent][algorithm_name]

        widgets["total"].config(text=f"Total Combinations : {result.get('total_generated', '-')}")
        widgets["valid"].config(text=f"Feasible Nodes : {result.get('valid_count', '-')}")

        invalid_count = result.get("pruned_count", result.get("invalid_count", "-"))
        widgets["invalid"].config(text=f"Pruned / Infeasible : {invalid_count}")

        top3 = result.get("top_3", [])
        for i in range(3):
            label = widgets[f"top{i+1}"]
            if i < len(top3):
                sol = top3[i]
                label.config(text=f"#{i+1} Tabungan:{sol['tabungan']}% | Emas:{sol['emas']}% | Reksa:{sol['reksa']}%")
            else:
                label.config(text=f"#{i+1} -")

        widgets["best"].config(
            text=f"Portfolio  ➔  T: {result['tabungan']}% | E: {result['emas']}% | R: {result['reksa']}%\n"
                 f"Wealth Max ➔  Rp {result['wealth']:,.0f}"
        )

        widgets["runtime"].config(text=f" ⏱ Execution Time: {result['runtime']:.6f}s")

    def run_optimization(self):
        try:
            modal = float(self.modal_entry.get())
        except ValueError:
            print("Modal tidak valid")
            return

        scenarios = [
            (3.5, self.tab1),
            (4.0, self.tab2),
            (4.5, self.tab3)
        ]

        for risk_limit, tab in scenarios:
            bb_result = branch_and_bound(modal, risk_limit)
            dp_result = dynamic_programming(modal, risk_limit)
            ga_result = genetic_algorithm(modal, risk_limit)

            self.update_algorithm_card(tab, "Branch and Bound", bb_result)
            self.update_algorithm_card(tab, "Dynamic Programming", dp_result)
            self.update_algorithm_card(tab, "Genetic Algorithm", ga_result)


if __name__ == "__main__":
    root = tk.Tk()
    app = InvestmentOptimizerGUI(root)
    root.mainloop()