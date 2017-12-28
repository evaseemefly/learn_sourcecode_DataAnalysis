# -*- coding: utf-8 -*-

"""
    作者:     梁斌
    版本:     1.0
    日期:     2017/10
    实战案例4-2：根据可穿戴设备识别用户行为
    该文件中的输出改为英文，可用于在不支持中文输出的服务器或机器上进行运行

    该案例有配套的讲解版本，在jupyter演示版中可找到

    声明：小象学院拥有完全知识产权的权利；只限于善意学习者在本课程使用，
         不得在课程范围外向任何第三方散播。任何其他人或机构不得盗版、复制、仿造其中的创意，
         我们将保留一切通过法律手段追究违反者的权利
"""

# 引入必要的包
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import GridSearchCV


# 解决matplotlib显示中文问题
# 仅适用于Windows
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# MacOS请参考 http://wenda.chinahadoop.cn/question/5304 修改字体配置

# 指定数据集路径
# 说明：该数据集和第四讲的数据集相同，学员请拷贝到data目录下
dataset_path = '../data'
train_datafile = os.path.join(dataset_path, 'train.csv')
test_datafile = os.path.join(dataset_path, 'test.csv')

# cv
cv_val = 3


def train_model(X_train, y_train, X_test, y_test, model_config):
    """
        返回对应的最优分类器及在测试集上的准确率
    """
    model = model_config[0]
    parameters = model_config[1]

    if parameters is not None:
        # 需要调参的模型
        clf = GridSearchCV(model, parameters, cv=cv_val, scoring='accuracy')
        clf.fit(X_train, y_train)
        print('Best parameters: ', clf.best_params_)
        print('Best score on validation set: {:.3f}', clf.best_score_)
    else:
        # 不需要调参的模型，如朴素贝叶斯
        model.fit(X_train, y_train)
        clf = model

    test_acc = clf.score(X_test, y_test)
    print('Score on test set: {:.3f}'.format(test_acc))
    return clf, test_acc


def main():
    """
        主函数
    """
    # 加载数据
    train_data = pd.read_csv(train_datafile)
    test_data = pd.read_csv(test_datafile)

    # 任务1. 数据查看
    print('\n===================== Task1. Inspect Data =====================')
    print('{} records in training set.'.format(len(train_data)))
    print('{} records in test set.'.format(len(test_data)))

    # 构建训练测试数据
    # 特征处理
    feat_names = train_data.columns[:-2].tolist()
    X_train = train_data[feat_names].values
    print('Feature dimensionality: {}.'.format(X_train.shape[1]))
    X_test = test_data[feat_names].values

    # 标签处理
    train_labels = train_data['Activity'].values
    test_labels = test_data['Activity'].values

    # 使用sklearn.preprocessing.LabelEncoder进行类别标签处理
    label_enc = LabelEncoder()
    y_train = label_enc.fit_transform(train_labels)
    y_test = label_enc.transform(test_labels)

    print('Target classes: ', label_enc.classes_)
    for i in range(len(label_enc.classes_)):
        print('Coding {} -- Label {}.'.format(i, label_enc.inverse_transform(i)))

    # 任务2. 特征处理
    print('\n===================== Task2. Feature Processing =====================')
    # 使用两种不同的scaler对特征进行处理
    # 1. min max scaler
    min_max_scaler = MinMaxScaler()
    X_train_min_max_scaled = min_max_scaler.fit_transform(X_train)
    X_test_min_max_scaled = min_max_scaler.transform(X_test)

    # 2. standard scaler
    std_scaler = StandardScaler()
    X_train_std_scaled = std_scaler.fit_transform(X_train)
    X_test_std_scaled = std_scaler.transform(X_test)

    # 任务3. 数据建模及参数调整
    print('\n===================== Task3. Modeling and Evaluation =====================')
    model_dict = {'kNN': (KNeighborsClassifier(), {'n_neighbors': [5, 10, 15]}),
                  'LR': (LogisticRegression(), {'C': [0.01, 1, 100]}),
                  'SVM': (SVC(), {'C': [100, 1000, 10000]}),
                  'DT': (DecisionTreeClassifier(), {'max_depth': [50, 100, 150]}),
                  'GNB': (GaussianNB(), None),
                  'RF': (RandomForestClassifier(), {'n_estimators': [100, 150, 200]}),
                  'GBDT': (GradientBoostingClassifier(), {'learning_rate': [0.1, 1, 10]})}

    results_df = pd.DataFrame(columns=['Not Scaled (%)', 'Min Max Scaled (%)', 'Std Scaled (%)'],
                              index=list(model_dict.keys()))
    results_df.index.name = 'Model'

    for model_name, model_config in model_dict.items():
        print('Traing model: ', model_name)
        print('Not Scaled')
        _, acc1 = train_model(X_train, y_train,
                              X_test, y_test,
                              model_config)

        print('Min Max Scaled')
        _, acc2 = train_model(X_train_min_max_scaled, y_train,
                              X_test_min_max_scaled, y_test,
                              model_config)

        print('Std Scaled')
        _, acc3 = train_model(X_train_std_scaled, y_train,
                              X_test_std_scaled, y_test,
                              model_config)
        print()

        results_df.loc[model_name] = [acc1 * 100, acc2 * 100, acc3 * 100]

    results_df.to_csv('./pred_results.csv')

    plt.figure(figsize=(10, 4))
    results_df.plot(kind='bar')
    plt.ylim([75, 105])
    plt.ylabel('Accuracy (%)')
    plt.tight_layout()
    plt.savefig('./pred_results.png')
    plt.show()


if __name__ == '__main__':
    main()
