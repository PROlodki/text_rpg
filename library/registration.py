from data.users import User
from data.character import Character
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import db_session
from library.debug_func.user_default import user_default
from library.debug_func.char_defaut import char_default


def register_user(update):
    reply_keyboard = [['/help', '/start', '/Record']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    user_info = update.effective_user
    db_sess = db_session.create_session()
    if not db_sess.query(User).filter(User.tg_id == update.effective_user.id).first():
        user = User(
            tg_id=update.effective_user.id,
            score=0,
            best_score=0,
            in_game=False)
        db_sess.add(user)
        db_sess.commit()

    update.message.reply_text(f'Добро пожаловать в EndlessDungeon, {user_info["first_name"]}!',
                              reply_markup=markup)


def register_char(update, context):
    db_sess = db_session.create_session()
    user_info = update.effective_user
    if not db_sess.query(Character).filter(Character.user_id == update.effective_user.id).first():
        user_character = Character(
            user_id=user_info.id,
            room_id=0,
            name=update.message.text)
        db_sess.add(user_character)
        db_sess.commit()
    reply_keyboard = [['/Запад', '/Север', '/Восток']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text(f'Поздравляем с созданием персонажа!), {user_info["first_name"]}!',
                              reply_markup=markup)
    char_default(update)
