import streamlit as st

st.title("Bookshop")

# 初始化session state
if 'purchases' not in st.session_state:
    st.session_state.purchases = []

# 模拟书籍数据
books = [
    {"id": 1, "title": "Python编程入门", "price": 59.99},
    {"id": 2, "title": "Streamlit实战", "price": 49.99},
    {"id": 3, "title": "机器学习基础", "price": 79.99}
]

# 用户购买界面
st.header("书籍列表")
for book in books:
    col1, col2, col3 = st.columns([6, 2, 2])
    with col1:
        st.write(f"**{book['title']}**")
    with col2:
        st.write(f"¥{book['price']}")
    with col3:
        if st.button(f"购买", key=f"buy_{book['id']}"):
            st.session_state.purchases.append(book)
            st.success(f"已添加 {book['title']} 到购物车!")

# 购物车显示
if st.session_state.purchases:
    st.header("您的购物车")
    for item in st.session_state.purchases:
        st.write(f"- {item['title']} (¥{item['price']})")

# 管理员视图
if st.checkbox("显示管理员面板"):
    st.header("管理员面板 - 最新购买记录")
    if st.session_state.purchases:
        for purchase in reversed(st.session_state.purchases):
            st.write(f"- {purchase['title']} (¥{purchase['price']})")
    else:
        st.write("暂无购买记录")

