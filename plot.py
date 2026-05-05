import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_data(csv_file, title, x_label, output_file):
    df = pd.read_csv(csv_file)
    
    # Standardiser le nom de la colonne d'instances
    if 'Nb instances' in df.columns:
        df.rename(columns={'Nb instances': 'NB instances'}, inplace=True)
        
    # Convertir le temps en secondes pour correspondre à l'image
    df['AVG_TIME_S'] = df['AVG_TIME'] / 1000.0
    
    # Configuration du style global
    sns.set_theme(style="white")
    plt.figure(figsize=(10, 7))
    
    # Création du barplot
    ax = sns.barplot(
        data=df, 
        x='PARAM', 
        y='AVG_TIME_S', 
        color='#7CB5EC',  # Bleu clair
        edgecolor='black', # Bordure noire
        linewidth=1.2,
        capsize=0,         # Pas de tiret sur la barre d'erreur
        err_kws={'color': 'black', 'linewidth': 1.5} # Ligne d'erreur noire et propre
    )
    
    # Ajout de la grille en pointillés
    ax.grid(axis='y', linestyle='--', color='#E0E0E0', zorder=0)
    ax.set_axisbelow(True) # La grille passe derrière les barres
    
    # Suppression des bordures haut et droite
    sns.despine()
    
    # Ajustement automatique des marges
    ax.set_ylim(0, ax.get_ylim()[1] * 1.1)
    
    plt.title(title, fontsize=16, pad=15, color='#333333')
    plt.xlabel(x_label, fontsize=12, color='#333333')
    plt.ylabel('Temps moyen par requête (s)', fontsize=12, color='#333333')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    plt.close()

# Créer les plots
plot_data('out/conc.csv', 'Temps moyen par requête selon la concurrence', 'Nombre d\'utilisateurs concurrents', 'out/conc.png')
plot_data('out/fanout.csv', 'Temps moyen par requête selon la taille (Nombre de followees)', 'Nb de followees', 'out/fanout.png')
