import scala.io.Source
import scala.util.Using
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
/**
 *  Скрипт-example чтения и вывода на экран Markdowm-файла
 *
 *  Для вывода на экран содержимого файла, необходимо вызвать 
 *  метод displayEnhanced(filePath: String) из объекта RichMarkdownReader
 */

// Класс статистики md - файла
case class MDStats(
  chars_cnt: Int,   // Количество символов
  lines_cnt: Int,   // Количество строк
  headers_cnt: Int, // Количество заголовков
  blocks_cnt: Int,  // Количество блоков кода
  links_cnt: Int,   // Количество ссылок
  images_cnt: Int   // Количество картинок
)

// Цвет текста
val COLOR = Map(
    // Текст для информационны сообщений
    "success" -> "\u001b[32m",
    "error"   -> "\u001b[31m",
    "info"    -> "\u001b[34m",
    "warn"    -> "\u001b[33m",  
    // Текст MD
    "header"  -> "\u001b[35m",  // Текст заголовка
    "bold"    -> "\u001b[1m",   // Жирный текст 
    "white"   -> "\u001b[2m",   // белый текст (Обычное сообщение)
     // Сброс
    "RESET" -> "\u001b[0m" 
  )

// Объект для чтения markdown - файла
object RichMarkdownReader {
    
  def caclMarkdownWithStats(filePath: String): Either[String, (String, MDStats)] = {
    Using(Source.fromFile(filePath)) { source =>
      val content = source.mkString
      val stats = analyzeMarkdown(content)
      (content, stats)
    }.toEither.left.map(_.getMessage)
  }

  private def analyzeMarkdown(content: String): MDStats = {
    val lines = content.split("\n")
    MDStats(
      chars_cnt = content.length,
      lines_cnt = lines.length,
      headers_cnt = lines.count(_.matches("^#{1,6}\\s+.*")),
      blocks_cnt = content.split("```").length / 2,
      links_cnt = "\\[.*?\\]\\(.*?\\)".r.findAllIn(content).length,
      images_cnt = "!\\[.*?\\]\\(.*?\\)".r.findAllIn(content).length
    )
  }
  /**
   * Читает фвйл markdown, выводит статистику и содержание файла (630 символов)
   * @param filePath путь и имя файла markdown
  */
  def displayEnhanced(filePath: String): Unit = {
    val timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
    
    println(s"${COLOR("info")}${COLOR("bold")}")
    println("╔══════════════════════════════════════════════════════════════╗")
    println("║                 📖 MARKDOWN RICH TEXT                        ║")
    println("╚══════════════════════════════════════════════════════════════╝")
    println(s"${COLOR("RESET")}")
    
    println(s"${COLOR("white")}⏰ Время: $timestamp${COLOR("RESET")}")
    println(s"${COLOR("info")}📁 Файл: $filePath${COLOR("RESET")}\n")

    caclMarkdownWithStats(filePath) match {
      case Right((content, stats)) =>
        displaySuccess(content, stats)
      case Left(error) =>
        displayError(error)
    }
  }

  private def displaySuccess(content: String, stats: MDStats): Unit = {
    println(s"${COLOR("success")}✅ ФАЙЛ УСПЕШНО ПРОЧИТАН${COLOR("RESET")}\n")
    
    // Статистика в красивой таблице
    println(s"${COLOR("header")}${COLOR("bold")}📊 СТАТИСТИКА:${COLOR("RESET")}")
    println( "┌────────────────────┬──────────┐")
    println(f"│ Кол-во символов    │ ${stats.chars_cnt}%8d │")
    println(f"│ Кол-во строк       │ ${stats.lines_cnt}%8d │")
    println(f"│ Кол-во заголовков  │ ${stats.headers_cnt}%8d │")
    println(f"│ Кол-во блоков      │ ${stats.blocks_cnt}%8d │")
    println(f"│ Кол-во ссылок      │ ${stats.links_cnt}%8d │")
    println(f"│ Кол-во изображений │ ${stats.images_cnt}%8d │")
    println( "└────────────────────┴──────────┘\n")
    
    // Превью контента
    println(s"${COLOR("header")}${COLOR("bold")}👀 ПРЕВЬЮ СОДЕРЖИМОГО:${COLOR("RESET")}")
    println("═" * 60)
    displayFormattedPreview(content.take(630))
    
    if (content.length > 630) {
      println(s"\n${COLOR("white")}... (показано первые 630 символов)${COLOR("RESET")}")
    }
  }

  private def displayError(error: String): Unit = {
    println(s"${COLOR("error")}❌ ОШИБКА ЧТЕНИЯ ФАЙЛА${COLOR("RESET")}\n")
    println( "┌──────────────────────────────────────────────────────────────┐")
    println(s"│ ${COLOR("error")}$error${COLOR("RESET")}${" "*(61-error.length)}│")
    println( "└──────────────────────────────────────────────────────────────┘")
  }

  private def displayFormattedPreview(content: String): Unit = {
    content.split("\n").take(11).foreach { line =>
      line.trim match {
        case h if h.startsWith("# ") => 
          println(s"${COLOR("header")}${COLOR("bold")}🔥 ${h.drop(2)}${COLOR("RESET")}")
        case h if h.startsWith("## ") => 
          println(s"${COLOR("info")}${COLOR("bold")}⚡ ${h.drop(3)}${COLOR("RESET")}")
        case h if h.startsWith("### ") => 
          println(s"${COLOR("warn")}💡 ${h.drop(4)}${COLOR("RESET")}")
        case code if code.startsWith("```") => 
          println(s"${COLOR("success")}📝 [Блок кода]${COLOR("RESET")}")
        case bullet if bullet.startsWith("- ") || bullet.startsWith("* ") => 
          println(s"   ${COLOR("warn")}▶${COLOR("RESET")} ${bullet.drop(2)}")
        case empty if empty.isEmpty => 
          println()
        case normal if normal.nonEmpty => 
          println(s"   $normal")
      }
    }
  }
}
