import tkinter as tk
from tkinter import ttk


class InvestmentOptimizerGUI:

    def configure_styles(self):

        style = ttk.Style()

        style.theme_use("clam")

        # Notebook
        style.configure(
            "TNotebook",
            background="#0f172a",
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            padding=(20, 10),
            background="#1e293b",
            foreground="white"
        )

        style.map(
            "TNotebook.Tab",
            background=[
                ("selected", "#22c55e")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        # Card
        style.configure(
            "Card.TLabelframe",
            background="#111827",
            foreground="white",
            borderwidth=1
        )

        style.configure(
            "Card.TLabelframe.Label",
            background="#111827",
            foreground="white",
            font=("Segoe UI", 11, "bold")
        )

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Investment Optimization System"
        )

        self.root.geometry(
            "1400x900"
        )

        self.root.configure(
            bg="#0f172a"
        )

        self.root.minsize(
            1000,
            700
        )

        self.configure_styles()
        self.create_widgets()

    # =================================
    # UI COMPONENTS
    # =================================


    def create_widgets(self):

        # =============================
        # HEADER
        # =============================

        header_frame = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        header_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        title_label = tk.Label(
            header_frame,
            text="INVESTMENT OPTIMIZATION SYSTEM",
            font=("Segoe UI", 22, "bold"),
            fg="white",
            bg="#0f172a"
        )

        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text=(
                "Comparative Analysis of "
                "Branch and Bound, "
                "Dynamic Programming, "
                "and Genetic Algorithm"
            ),
            font=("Segoe UI", 10),
            fg="#94a3b8",
            bg="#0f172a"
        )

        subtitle_label.pack(
            pady=(5, 0)
        )

        top_frame = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        top_frame.pack(
            fill="x",
            padx=20
        )

        input_card = ttk.LabelFrame(
            top_frame,
            text="Input Parameter",
            style="Card.TLabelframe"
        )

        risk_card = ttk.LabelFrame(
            top_frame,
            text="Risk Limit Scenario",
            style="Card.TLabelframe"
        )

        input_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0,10)
        )

        risk_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        # =================================
        # INPUT CARD CONTENT
        # =================================

        input_content = tk.Frame(
            input_card,
            bg="#111827"
        )

        input_content.pack(
            fill="both",
            padx=15,
            pady=15
        )

        tk.Label(
            input_content,
            text="Modal Awal (Rp)",
            bg="#111827",
            fg="white",
            font=("Segoe UI", 10)
        ).pack(
            anchor="w"
        )

        self.modal_entry = tk.Entry(
            input_content,
            font=("Segoe UI", 11),
            width=25
        )

        self.modal_entry.pack(
            pady=(8, 15),
            anchor="w"
        )

        self.modal_entry.insert(
            0,
            "100000000"
        )

        self.run_button = tk.Button(
            input_content,
            text="▶ Jalankan Optimasi",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=20,
            pady=8
        )

        self.run_button.pack(
            anchor="w"
        )

        # =================================
        # RISK CARD CONTENT
        # =================================

        risk_content = tk.Frame(
            risk_card,
            bg="#111827"
        )

        risk_content.pack(
            fill="both",
            padx=15,
            pady=15
        )

        for text in [
            "🟢 3.5 (Conservative)",
            "🟡 4.0 (Moderate)",
            "🔴 4.5 (Aggressive)"
        ]:
            tk.Label(
                risk_content,
                text=text,
                bg="#111827",
                fg="white",
                font=("Segoe UI", 10)
            ).pack(
                anchor="w",
                pady=5
            )

        # =============================
        # NOTEBOOK
        # =============================

        self.notebook = ttk.Notebook(
            self.root
        )

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # =============================
        # TAB 1
        # =============================

        self.tab1 = ttk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.tab1,
            text="Scenario 1"
        )

        # =============================
        # TAB 2
        # =============================

        self.tab2 = ttk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.tab2,
            text="Scenario 2"
        )

        # =============================
        # TAB 3
        # =============================

        self.tab3 = ttk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.tab3,
            text="Scenario 3"
        )


if __name__ == "__main__":

    root = tk.Tk()

    app = InvestmentOptimizerGUI(
        root
    )

    root.mainloop()