import tkinter as tk
from tkinter import ttk
import sys
import os

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if project_root not in sys.path:
    sys.path.append(project_root)

from Algorithms.branch_bound import (
    branch_and_bound
)

from Algorithms.dynamic_programming import (
    dynamic_programming
)

from Algorithms.genetic_algorithm import (
    genetic_algorithm
)


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
        self.create_algorithm_cards(
            self.tab1
        )
        self.create_algorithm_cards(
            self.tab2
        )
        self.create_algorithm_cards(
            self.tab3
        )

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
            pady=8,
            command=self.run_optimization
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

        self.tab1 = tk.Frame(
            self.notebook,
            bg="#0f172a"
        )

        self.notebook.add(
            self.tab1,
            text="Scenario 1"
        )

        # =============================
        # TAB 2
        # =============================

        self.tab2 = tk.Frame(
            self.notebook,
            bg="#0f172a"
        )

        self.notebook.add(
            self.tab2,
            text="Scenario 2"
        )

        # =============================
        # TAB 3
        # =============================

        self.tab3 = tk.Frame(
            self.notebook,
            bg="#0f172a"
        )

        self.notebook.add(
            self.tab3,
            text="Scenario 3"
        )

    def update_algorithm_card(
        self,
        parent,
        algorithm_name,
        result
    ):

        widgets = self.algorithm_widgets[
            parent
        ][algorithm_name]

        widgets["total"].config(
            text=f"Total Kombinasi : {result.get('total_generated', '-')}"
        )

        widgets["valid"].config(
            text=f"Valid : {result.get('valid_count', '-')}"
        )

        invalid_count = (
            result.get(
                "pruned_count",
                result.get(
                    "invalid_count",
                    "-"
                )
            )
        )

        widgets["invalid"].config(
            text=f"Invalid / Pruned : {invalid_count}"
        )

        top3 = result.get(
            "top_3",
            []
        )

        for i in range(3):

            label = widgets[f"top{i+1}"]

            if i < len(top3):

                sol = top3[i]

                label.config(
                    text=(
                        f"#{i+1} "
                        f"T:{sol['tabungan']}% "
                        f"E:{sol['emas']}% "
                        f"R:{sol['reksa']}%"
                    )
                )

            else:

                label.config(
                    text=f"#{i+1} -"
                )

        widgets["best"].config(
            text=(
                f"T:{result['tabungan']}% | "
                f"E:{result['emas']}% | "
                f"R:{result['reksa']}%\n"
                f"Wealth: Rp {result['wealth']:,.0f}"
            )
        )

        widgets["runtime"].config(
            text=(
                f"Runtime : "
                f"{result['runtime']:.6f} detik"
            )
        )

    def create_algorithm_cards(
    self,
    parent
):

        container = tk.Frame(
            parent,
            bg="#0f172a"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # 3 kolom sama besar
        container.grid_columnconfigure(
            0,
            weight=1
        )

        container.grid_columnconfigure(
            1,
            weight=1
        )

        container.grid_columnconfigure(
            2,
            weight=1
        )

        container.grid_rowconfigure(
            0,
            weight=1
        )

        cards = [
            "Branch and Bound",
            "Dynamic Programming",
            "Genetic Algorithm"
        ]

        for index, title in enumerate(cards):

            card = ttk.LabelFrame(
                container,
                text=title,
                style="Card.TLabelframe"
            )

            card.grid(
                row=0,
                column=index,
                sticky="nsew",
                padx=8,
                pady=5
            )

            content = tk.Frame(
                card,
                bg="#111827"
            )

            content.pack(
                fill="both",
                expand=True,
                padx=10,
                pady=10
            )

            stats_title = tk.Label(
                content,
                text="STATISTICS",
                bg="#111827",
                fg="#22c55e",
                font=("Segoe UI", 10, "bold")
            )

            stats_title.pack(
                anchor="w"
            )

            total_label = tk.Label(
                content,
                text="Total Kombinasi : -",
                bg="#111827",
                fg="white"
            )

            total_label.pack(
                anchor="w"
            )

            valid_label = tk.Label(
                content,
                text="Valid : -",
                bg="#111827",
                fg="white"
            )

            valid_label.pack(
                anchor="w"
            )

            invalid_label = tk.Label(
                content,
                text="Invalid / Pruned : -",
                bg="#111827",
                fg="white"
            )

            invalid_label.pack(
                anchor="w"
            )

            ttk.Separator(
                content,
                orient="horizontal"
            ).pack(
                fill="x",
                pady=10
            )

            top_title = tk.Label(
                content,
                text="TOP 3 SOLUTIONS",
                bg="#111827",
                fg="#22c55e",
                font=("Segoe UI", 10, "bold")
            )

            top_title.pack(
                anchor="w"
            )

            top1 = tk.Label(
                content,
                text="#1 -",
                bg="#111827",
                fg="white"
            )

            top1.pack(
                anchor="w",
                pady=2
            )

            top2 = tk.Label(
                content,
                text="#2 -",
                bg="#111827",
                fg="white"
            )

            top2.pack(
                anchor="w",
                pady=2
            )

            top3 = tk.Label(
                content,
                text="#3 -",
                bg="#111827",
                fg="white"
            )

            top3.pack(
                anchor="w",
                pady=2
            )

            ttk.Separator(
                content,
                orient="horizontal"
            ).pack(
                fill="x",
                pady=10
            )

            best_title = tk.Label(
                content,
                text="BEST SOLUTION",
                bg="#111827",
                fg="#22c55e",
                font=("Segoe UI", 10, "bold")
            )

            best_title.pack(
                anchor="w"
            )

            best_label = tk.Label(
                content,
                text="-",
                bg="#111827",
                fg="white",
                justify="left"
            )

            best_label.pack(
                anchor="w",
                pady=5
            )

            ttk.Separator(
                content,
                orient="horizontal"
            ).pack(
                fill="x",
                pady=10
            )

            runtime_label = tk.Label(
                content,
                text="Runtime : -",
                bg="#111827",
                fg="#facc15"
            )

            runtime_label.pack(
                anchor="w"
            )

            if not hasattr(
                self,
                "algorithm_widgets"
            ):
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

    def run_optimization(self):

        try:

            modal = float(
                self.modal_entry.get()
            )

        except ValueError:

            print(
                "Modal tidak valid"
            )

            return

        scenarios = [
            (3.5, self.tab1),
            (4.0, self.tab2),
            (4.5, self.tab3)
        ]

        for risk_limit, tab in scenarios:

            bb_result = branch_and_bound(
                modal,
                risk_limit
            )

            dp_result = dynamic_programming(
                modal,
                risk_limit
            )

            ga_result = genetic_algorithm(
                modal,
                risk_limit
            )

            self.update_algorithm_card(
                tab,
                "Branch and Bound",
                bb_result
            )

            self.update_algorithm_card(
                tab,
                "Dynamic Programming",
                dp_result
            )

            self.update_algorithm_card(
                tab,
                "Genetic Algorithm",
                ga_result
            )

if __name__ == "__main__":

    root = tk.Tk()

    app = InvestmentOptimizerGUI(
        root
    )

    root.mainloop()