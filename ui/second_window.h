#ifndef SECOND_WINDOW_H
#define SECOND_WINDOW_H

#include <QMainWindow>

namespace Ui {
class second_window;
}

class second_window : public QMainWindow
{
    Q_OBJECT

public:
    explicit second_window(QWidget *parent = nullptr);
    ~second_window();

private:
    Ui::second_window *ui;
};

#endif // SECOND_WINDOW_H
