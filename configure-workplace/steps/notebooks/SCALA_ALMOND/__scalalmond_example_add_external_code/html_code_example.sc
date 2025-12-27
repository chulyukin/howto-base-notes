import almond.display.Html
import almond.interpreter.api.DisplayData
/**
 *  Скрипт-example с функциями html вывода
 *
 *  html_print - Выаод текста с заголовком на экран в html-формате
 *  html_table - Выаод таблицы на экран в html-формате
 *  html_report - Выаод простого отчета на экран в html-формате
 */

/**
 * Выаод текста с заголовком на экран в html-формате
 * @param h Текст заголовка
 * @param text Текст для вывода на экран
 */
def html_print (h: String, text: String ): Html = {
    Html(
  s"""<div style="padding: 20px; background-color: #f0f0f0; border-radius: 10px;">
       <h2 style="color: #333;">$h</h2>
       <p style="color: #666;">$text</p>
     </div>""")
    
}

/**
 * Выаод таблицы на экран в html-формате
 *
 * @param headers Seq с заголовками столбцов таблицы
 * @param data Seq со строками данных таблицы
 * @param width Отностиельный размер таблицы на экране
*/
def html_table(headers: Seq[String], data: Seq[Seq[Any]], width: String = "35%"): Html = {
  
  // Функция для выбора выравнивания по типу элемента
  def align(item: Any): String = item match {
    case s: String => "left"
    case s         => "right"
  }
  
  // Генерация HTML для заголовков.
  val headersHtml: String = headers.map { h =>
    s"<th style='padding: 12px; text-align: left;'>$h</th>"
  }.mkString("\n")

  // Генерация HTML для строк данных
  val rowsHtml: String = data.map { row =>
    val rowHtml = row.map { item =>
      // Применяем функцию align для каждого элемента строки
      val alignment = align(item)
      s"<td style='padding: 8px; text-align: $alignment;'>$item</td>"
    }.mkString("\n")
    s"<tr>\n$rowHtml\n</tr>"
  }.mkString("\n")

  // Формирование итоговой таблицы
  Html(s"""
    <table style="border-collapse: collapse; width: $width;">
      <thead>
        <tr style="background-color: #4CAF50; color: white;">
          $headersHtml
        </tr>
      </thead>
      <tbody>
        $rowsHtml
      </tbody>
    </table>
  """)
}

case class Report(title: String, data: Map[String, Double]) {
  def toHTML: String = {
    val items = data.map { case (k, v) =>
      s"""<div style="margin: 10px 0;">
           <strong>$k:</strong> 
           <span style="color: #219A00; font-size: 1.2em;">${"%.2f".format(v)}</span>
         </div>"""
    }.mkString("\n")
    
    s"""<div style="border: 2px solid #ddd; padding: 20px; border-radius: 8px;">
         <h3 style="margin-top: 0; color: #FBA;">$title</h3>
         $items
       </div>"""
  }
}

/**
 * Выаод простого отчета на экран в html-формате
 *
 * @param reportH Текст заголовка отчета
 * @param reportH Выводимые данные отчета в формате "показатель, значение"
 */
def html_report(reportH: String, reportB: Map[String,Double]): Unit = {
    // Создаем объект Report
    val report = Report(reportH, reportB)

    // Отображаем HTML-представление отчета
    kernel.publish.html(report.toHTML)
    }