import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc
import pyspark.sql.functions as f_
import matplotlib.pyplot as plt
import seaborn as sns

#========================================================================================================#
#                                      ФУНКЦИИ ВИЗУАЛЗАЦИИ МЕТРИК                                        #
#                                                                                                        #
#        shap_plot                    - визуализация SHAP Values                                         #
#        confusion_matrix_plot        - визуализация Confusion Matrix                                    #
#        precission_recall_curve_plot - визуализация SHAP Values                                         #
#        roc_auc_curve_plot           -                                                                  #
#        roc_auc_compare_plot         -                                                                  # 
#========================================================================================================#

#------------------------ SHAP

def shap_plot(sparkdf, top_fts_cnt
                        ,header = "Global Importance."
                        ,feature_mm = "feature_nm"
                        ,col_shap_val = "shap_value"
                ):
    """
    Функция визуализации SHAP Values. Выводит на экран диаграмму с фичами и их средним значением 
    влияния на prediction (avg(SHAP value)), по всему размеру sparkdf.

    Параметры:
        sparkdf - Spark DataFrame с расчетом значений Shap
        top_fts_cnt - Колияество топовых фичей для визуализации
        header - Название визуализации
        feature_mm - Колонка с наименованием фичей
        col_shap_val - Колонка с рассчитаными значениями Shap

    """
    # Pandas DataFrame с результатом группировки и расчета срденего значенеия abs(col_shap_val)
    pdf = sparkdf.groupBy(feature_mm).agg(f_.avg(f_.abs(col_shap_val)).alias(col_shap_val)) \
                 .orderBy(f_.abs(col_shap_val).desc())\
                 .limit(top_fts_cnt) \
                 .toPandas()
    # Bar plot
    plt.figure(figsize=(6.9, 2.8)) 
    bars = plt.barh(pdf[feature_mm], pdf[col_shap_val], color='#001014', zorder=3)
    
    # Оформление
    plt.title(f"SHAP {header} Топ {top_fts_cnt}.", fontsize=11, fontweight='bold', pad=10, loc ='left')
    plt.xlabel('Среднее влияние на prediction: avg(SHAP value)', fontsize=9)
    plt.ylabel('', fontsize=9)
    plt.grid(axis='x', linestyle='--', alpha=0.9, zorder=0) # Сетка по вертикали
    
    # Значение Data Labels на bar
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.005,        # X координата (значение + отступ)
                 bar.get_y() + bar.get_height()/2, # Y координата (центр бара)
                # Вертикальное выравнивание, шрифт + формат числа (3 знака)
                f'{width:.3f}', va='center', fontsize=9, color='black')  
        
    plt.xlim(0, pdf[col_shap_val].max() * 1.11) # Корректировка оси X, для цифр справа

    plt.tight_layout()
    plt.show()

#------------------------ CONFUSION MATRIX
def __mk_labels(cm):
    """Возвращает матрицу меток для отображения CONFUSION MATRIX """         
    names = ['TN (True Neg)', 'FP (False Pos)', 'FN (False Neg)',  'TP (True Pos)']
    counts = ["{0:0.0f}".format(value) for value in cm.flatten()]
    labels = [f"{v1}\n{v2}" for v1, v2 in zip(names, counts)]
    return np.asarray(labels).reshape(2,2)

def confusion_matrix_plot(train, test):
    """
    Выводит на экран 2 графика CONFUSION MATRIX для Train и Test

     Параметры:
        train - numpy array: [[TN, FP], [FN, TP]] для train DataSet
        test - numpy array: [[TN, FP], [FN, TP]] для test DataSet
        
     TP (True Positive) — верно предсказанные положительные
     TN (True Negative) — верно предсказанные отрицательные
     FP (False Positive) — ложные срабатывания
     FN (False Negative) — пропуски предсказания

    """  
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.6, 2.9))
    # График для TRAIN
    labels_train = __mk_labels(train)
    sns.heatmap(train, annot=labels_train, fmt='', cmap='Blues', ax=ax1, cbar=False, annot_kws={"fontsize":12})
    ax1.set_title('Матрица ошибок (TRAIN)')
    ax1.set_xlabel("Prediction"); ax1.set_ylabel('Target value')
    ax1.set_xticklabels(['0', '1']); ax1.set_yticklabels(['0', '1'])

    # График для TEST
    labels_test = __mk_labels(test)
    sns.heatmap(test, annot=labels_test, fmt='', cmap='Oranges', ax=ax2, cbar=False, annot_kws={"fontsize":12})
    ax2.set_title('Матрица ошибок (TEST)')
    ax2.set_xlabel('Prediction'); ax2.set_ylabel('Target value')

    plt.tight_layout()    
    plt.show()

#------------------------ PRECISSION/RECALL

def precission_recall_curve_plot(pdf_train, pdf_test):
    """
    Функция выводит на экран 3 графика рядом:
        - Train. Кривая Precision-Recall
        - Test. Кривая Precision-Recall
        - Зависимость PR от порога (Threshold)
        
    Параметры:
        pdf_train - Pandas DataFrame train
        pdf_test - Pandas DataFrame test

    Pandas DataFrame должен содержать колонки:
        - probability - колонка с расчитанными вероятностями
        - label - колонка с целевой пересенной
    """
    y_train_scores = pdf_train['probability']
    y_train_true = pdf_train['label']
    train_r, train_pr, thresholds_train = precision_recall_curve(y_train_true, y_train_scores)

    y_test_scores = pdf_test['probability']
    y_test_true = pdf_test['label']
    test_p, test_r, _ = precision_recall_curve(y_test_true, y_test_scores)    
    # --- График 1: Train ---    
    fig, (ax1, ax2, ax3 ) = plt.subplots(1, 3, figsize=(13.3, 4.3))
    ax1.plot(train_r, train_pr, color='purple', lw=2, label='PR Curve (Train)')
    ax1.fill_between(train_r, train_pr, alpha=0.2, color='purple')    
    ax1.set_title('Train. Кривая Precision-Recall')    
    ax1.set_xlabel('Recall (Полнота)')
    ax1.set_ylabel('Precision (Точность)') 
    ax1.grid(True)
    ax1.legend()
    # --- График 2: Test ---
    ax2.plot(test_r, test_p, color='navy', lw=2, label='PR Curve (Test)')
    ax2.fill_between(test_r, test_p, alpha=0.2, color='navy')
    ax2.set_title('Test. Кривая Precision-Recall')
    ax2.set_xlabel('Recall (Полнота)')
    ax2.set_ylabel('Precision (Точность)')
    ax2.grid(True)
    ax2.legend()

    ax3.plot(thresholds_train, train_pr[:-1], label="Precision (Точность)", color="blue")
    ax3.plot(thresholds_train, train_r[:-1], label="Recall (Полнота)", color="green")
    ax3.set_title('''Зависимость PR от порога (Threshold)''')
    ax3.set_xlabel('Порог классификации (Threshold)')
    ax3.set_ylabel('Значение метрики')
    ax3.legend(loc="lower left")
    ax3.grid(True)

    # Точка пересечения (баланс)
    idx = np.argwhere(np.diff(np.sign(train_pr[:-1] - train_r[:-1]))).flatten()
    if len(idx) > 0:
        i = idx[0] 
    
        balance_threshold = thresholds_train[i]
        balance_score = train_pr[i] 

        # Красная точка
        ax3.plot(balance_threshold, balance_score, 'ro')

        ax3.annotate(f'Баланс: {balance_threshold:.2f}', 
                 (balance_threshold, balance_score), # Тут теперь координаты (float, float)
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center')

    
    plt.tight_layout() # Чтобы подписи не накладывались друг на друга
    plt.show() # Чем ближе график к правому верхнему углу (1.0, 1.0), тем лучше модель

#------------------------ ROC AUC
def roc_auc_curve_plot(pdf):
    """
    Функция выводит на экран кривую Receiver Operating Characteristic (ROC):

     Параметры:
        pdf - Pandas DataFrame

    Pandas DataFrame должен содержать колонки:
        - probability - колонка с расчитанными вероятностями
        - label - колонка с целевой пересенной
    """
    
    fpr, tpr, thresholds = roc_curve(pdf['label'], pdf['probability'])
    # Площадь под кривой (AUC)
    roc_auc = auc(fpr, tpr)
    # Gini
    gini = 2 * roc_auc - 1   
    # Построение графика ---
    plt.figure(figsize=(6.3, 4.3))

    # Сама кривая
    plt.plot(fpr, tpr, color='darkorange', lw=2,  label=f'ROC curve (AUC = {roc_auc:.3f})')

    # Gini на график отдельным текстом или в легенду
    plt.text(0.6, 0.2, f'Gini = {gini:.3f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    # Диагональ (случайная модель, AUC=0.5)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Guess')
    
    # Область под кривой - заливка цветом (визуализация AUC)
    plt.fill_between(fpr, tpr, color='orange', alpha=0.1)
    # Настройки осей
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])

    plt.xlabel('False Positive Rate (FPR)')    
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

# Функция для расчета данных для графика
def __get_roc_data(y_true, y_scores):
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)
    gini = 2 * roc_auc - 1
    return fpr, tpr, gini

def roc_auc_compare_plot(pdf_train, pdf_test):
    """
    Функция выводит на экран кривую Receiver Operating Characteristic (ROC) для train и test

    Параметры:
        pdf_train - Pandas DataFrame train
        pdf_test - Pandas DataFrame test

    Pandas DataFrame должен содержать колонки:
        - probability - колонка с расчитанными вероятностями
        - label - колонка с целевой пересенной
    """
    
    y_train = pdf_train['label']
    y_scores_train =  pdf_train['probability']
    y_test = pdf_test['label']
    y_scores_test = pdf_test['probability']

    fpr_train, tpr_train, gini_train = __get_roc_data(y_train, y_scores_train)
    fpr_test, tpr_test, gini_test = __get_roc_data(y_test, y_scores_test)

    plt.figure(figsize=(6.3, 4.3))

    # Линия Train
    plt.plot(fpr_train, tpr_train, color='blue', linestyle='--', lw=2, label=f'Train (Gini = {gini_train:.1%})')

    # Линия Test
    plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test (Gini = {gini_test:.1%})')

    # Диагональ
    plt.plot([0, 1], [0, 1], color='grey', lw=1, linestyle='--')

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Сравнение ROC-кривых\nРазрыв Gini: {abs(gini_train - gini_test):.1%}') 
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()