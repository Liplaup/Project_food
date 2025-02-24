import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_uml_analysis_cover():
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Set the background color
    ax.set_facecolor('#f9f9f9')
    
    # Title
    ax.text(0.5, 0.9, "Dossier d'Analyse des Besoins",
             ha='center', va='center', fontsize=24, fontweight='bold', color='#333333')
    ax.text(0.5, 0.85, "par les Cas d'Utilisation UML",
             ha='center', va='center', fontsize=18, fontweight='bold', color='#555555')
    
    # UML Diagram Icon
    uml_icon = patches.Circle((0.25, 0.5), 0.15, facecolor='#007BFF', edgecolor='#0056b3', linewidth=2)
    ax.add_patch(uml_icon)
    ax.text(0.25, 0.5, "UML", ha='center', va='center', fontsize=20, color='white', fontweight='bold')
    
    # Cas d'Utilisation Icon
    use_case_icon = patches.Rectangle((0.55, 0.35), 0.3, 0.2, facecolor='#28a745', edgecolor='#218838', linewidth=2, angle=30)
    ax.add_patch(use_case_icon)
    ax.text(0.68, 0.45, "Cas d'Utilisation", ha='center', va='center', fontsize=14, color='white', fontweight='bold', rotation=30)
    
    # Arrow connecting UML and Use Case
    ax.arrow(0.35, 0.5, 0.2, 0, head_width=0.05, head_length=0.05, fc='black', ec='black', linewidth=1.5)
    
    # Additional text
    ax.text(0.5, 0.2, "Analyse des besoins par modélisation",
             ha='center', va='center', fontsize=16, color='#666666')
    
    # Hide axes
    ax.axis('off')
    
    # Show plot
    plt.show()

draw_uml_analysis_cover()