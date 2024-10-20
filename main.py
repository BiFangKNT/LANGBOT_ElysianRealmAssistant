from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import yaml
import re
import os


# 注册插件
@register(name="ElysianRealmAssistant", description="崩坏3往事乐土攻略助手", version="1.0", author="BiFangKNT")
class ElysianRealmAssistant(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        super().__init__(host)
        self.config = self.load_config()
        flow_types = [
            "蓄力", "分支", "普攻", "武器", "大招", "塑灵", "结命", 
            "安愈", "凋换", "板砖", "弹反", "混合", "星环", "睡觉"
        ]
        flow_pattern = "|".join(flow_types)
        
        self.url_pattern = re.compile(
            rf'''
            ^(?:
                ((.{{0,5}})乐土list) |                        # 匹配0-5个字符后跟"乐土list"
                (乐土推荐) |                                  # 匹配"乐土推荐"
                (?P<角色乐土>(.{{1,5}})乐土\d?) |             # 匹配1-5个字符后跟"乐土"，可选择性地跟随一个数字
                (?P<角色流派>(.{{1,5}})({flow_pattern})流)    # 匹配1-5个字符，后跟特定的流派名称
            )$
            ''',
            re.VERBOSE
        )
        self.recommendation = "赫丽娅星环流"
        self.update_date = "2024年10月14日"

    # 异步初始化
    async def initialize(self):
        pass

    @handler(PersonNormalMessageReceived)
    async def on_person_message(self, ctx: EventContext):
        await self.ElysianRealmAssistant(ctx)

    @handler(GroupNormalMessageReceived)
    async def on_group_message(self, ctx: EventContext):
        await self.ElysianRealmAssistant(ctx)

    def load_config(self):
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(plugin_dir, 'ElysianRealmConfig.yaml')
        
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            self.ap.logger.info(f"配置文件未找到: {config_path}")
            return {}
        except yaml.YAMLError as e:
            self.ap.logger.info(f"解析YAML文件时出错: {e}")
            return {}
        except Exception as e:
            self.ap.logger.info(f"加载配置文件时发生未知错误: {e}")
            return {}

    async def ElysianRealmAssistant(self, ctx: EventContext):
        # 检查消息是否已经被处理过
        if hasattr(ctx, 'message_processed'):
            self.ap.logger.info("消息已被处理，跳过")
            return

        msg = ctx.event.text_message

        # 输出信息
        self.ap.logger.info(f"乐土攻略助手正在处理消息: {msg}")

        # 如果正则表达式没有匹配成功，直接终止脚本执行
        if not self.url_pattern.search(msg):
            self.ap.logger.info("乐土攻略助手：格式不匹配，不进行处理")
            return

        optimized_message = self.convert_message(msg)

        if optimized_message:
            # 输出信息
            self.ap.logger.info(f"处理后的消息: {optimized_message}")

            # 回复消息
            if isinstance(optimized_message, tuple):
                text, image = optimized_message
                ctx.add_return('reply', text)
                ctx.add_return('reply', image)
            else:
                ctx.add_return('reply', optimized_message)

            # 阻止该事件默认行为
            ctx.prevent_default()

            # 记消息已被处理
            setattr(ctx, 'message_processed', True)
        else:
            self.ap.logger.info("消息处理后为空，不进行回复")

    def convert_message(self, message):
        if message == "乐土list":
            return yaml.dump(self.config, allow_unicode=True)

        if message == "乐土推荐":
            return self.handle_recommendation()

        if "乐土list" in message:
            return self.handle_list_query(message)

        return self.handle_normal_query(message)

    def handle_recommendation(self):
        for key, values in self.config.items():
            if self.recommendation in values:
                image_url = f"https://raw.githubusercontent.com/BiFangKNT/ElysianRealm-Data/refs/heads/master/{key}.jpg"
                return f"本期乐土推荐更新于{self.update_date}\n推荐为：\n", mirai.Image(url=image_url)
        return "未找到推荐的乐土攻略。"

    def handle_list_query(self, message):
        query = message.replace("list", "").strip()
        for key, values in self.config.items():
            if query in values:
                return yaml.dump({key: values}, allow_unicode=True)
        return "未找到相关的乐土信息。"

    def handle_normal_query(self, message):
        for key, values in self.config.items():
            if message in values:
                image_url = f"https://raw.githubusercontent.com/BiFangKNT/ElysianRealm-Data/refs/heads/master/{key}.jpg"
                return "攻略url为：\n", mirai.Image(url=image_url)
        return "未找到相关的乐土攻略。"

    # 插件卸载时触发
    def __del__(self):
        pass
