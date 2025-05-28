import sys
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import seaborn as sns

from src.exception import CustomException
from src.logger import logging
from src.utils import SaveChart

save_chart = SaveChart()

class chartGenerator:
    def __init__(self, data):
        self.data = data


    def barchart_of_titles(self, n=10):
        df = self.data
        title_counts = df['domain'].value_counts().head(n)

        titles = title_counts.index
        counts = title_counts.values

        fig, ax = plt.subplots(figsize=(12, 7))

       
        colors = cm.Blues(np.linspace(0.4, 0.9, n))

        bars = ax.barh(titles, counts, color=colors)

       
        ax.set_title(f'Top {n} Domains Visited', fontsize=18, weight='bold', pad=20)
        ax.set_xlabel("Visit Frequency", fontsize=12)
        ax.set_ylabel("Domain", fontsize=12)

        
        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                    f'{int(width)}', va='center', ha='left', fontsize=10)

        
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        ax.invert_yaxis() 
        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()

        
        save_chart = SaveChart()
        save_chart.save(fig, filename="Most_visited_domain")

    def user_activity_time(self):
        df = self.data
        counts = df['time_of_day'].value_counts()

        
        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, autotexts = ax.pie(
            counts,
            labels=counts.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Pastel1.colors,
            textprops={'fontsize': 10}
        )

        ax.set_title("User Activity Distribution by Time of Day", fontsize=14)

        
        save_chart = SaveChart()
        save_chart.save(fig, filename='Most_active_time')

    def domains_after_inactivity(self, threshold):
        df =self.data
        long_inactivity_df = df[df['inactivity'] >= threshold]
        domain_counts = long_inactivity_df['domain'].value_counts()

        fig, ax = plt.subplots(figsize=(12, 8))
        colors = cm.Blues(np.linspace(0.4, 0.9, len(domain_counts)))
        bars = ax.barh(domain_counts.index, domain_counts.values, color=colors)
        ax.set_title("Most Frequent Domains After Long Inactivity", fontsize=16, weight='bold', pad=20)
        ax.set_xlabel("Domain", fontsize=12)
        ax.set_ylabel("Visit Frequency", fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        for bar in bars:
            width = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, width + 1, f'{int(width)}', ha='center', fontsize=10)
        save_chart.save(fig,filename="Domains after 6 hrs window")
        plt.tight_layout()


    def most_typed_domains(self, n=10):
        df = self.data
        df = df[df['transition'] == 'typed']
        domain_counts = df['domain'].value_counts().head(n)
        titles = domain_counts.index
        counts = domain_counts.values
        fig, ax = plt.subplots(figsize=(12, 7))
        colors = cm.Blues(np.linspace(0.4, 0.9, n))
        bars = ax.barh(titles, counts, color=colors)

        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                    f'{int(width)}', va='center', ha='left', fontsize=10)

        ax.set_title(f'Top {n} Most Typed Domains', fontsize=18, weight='bold', pad=20)
        ax.set_xlabel("Frequency of Typing", fontsize=12)
        ax.set_ylabel("Domain", fontsize=12)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.invert_yaxis()  
        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()
        save_chart.save(fig, filename="Most typed domains")

    def inactivity_by_date(self):
        df = self.data

        fig = plt.figure(figsize=(12, 6))
        plt.plot(df['eventtime'], df['inactivity'], color='blue', linewidth=2, label='Inactivity')
        plt.xlabel('Event Time', fontsize=12)
        plt.ylabel('Inactivity (minutes)', fontsize=12)
        plt.title('Inactivity vs Event Time', fontsize=14)
        plt.xticks(rotation=45)  
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        save_chart.save(fig, filename="inactivity_by_date")

    def domain_exit_point(self):
        df = self.data.copy()
        
        
        df['prev_domain'] = df['domain'].shift(1)
        df['domain_change'] = df['domain'] != df['prev_domain']

        
        domain_change_pages = df[df['domain_change']]['title']
        page_counts = domain_change_pages.value_counts().head(10)

        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x=page_counts.values, y=page_counts.index, palette="magma", ax=ax)

        ax.set_title('Top Pages Where Domain Changed (Exit Points)', fontsize=14, weight='bold')
        ax.set_xlabel('Number of Domain Changes')
        ax.set_ylabel('Page Title')
        plt.tight_layout()

        
        save_chart.save(fig, filename="Top Exit points of Domain")