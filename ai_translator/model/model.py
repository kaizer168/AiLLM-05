from book import ContentType

class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:
        return f"{text}"
        #return f"translate to {target_language}：{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        return f"\n{table}"
        #return f"translate to {target_language}，maintain row and column spacing (spaces, separators) and return in tabular form：\n{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt, target_language):
        raise NotImplementedError("子类必须实现 make_request 方法")
