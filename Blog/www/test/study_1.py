#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      admin
#
# Created:     12-07-2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


async def test(loop):
    await orm.create_pool(loop=loop, user='www-data',
                          password='www-data', db='awesome')
    # 经测试能够执行，保存一条数据成功。
    # u = User(name='test_name', email='test@test.com', admin=False, passwd='123',
             # image='about:blank', id='110')
    # await u.save()
    
    await orm.destory_pool()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()


if __name__ == '__main__':
    import sys
    sys.path.append("../")
    import orm
    from models import User, Blog, Comment
    import asyncio
    main()
