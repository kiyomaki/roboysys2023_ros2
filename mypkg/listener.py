#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query')  # サービスクライアントの作成
    while not client.wait_for_service(timeout_sec=1.0):  # サービスの待機
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "Maxi Kiyosawa"
    future = client.call_async(req)  # 非同期でサービスを呼び出し

    while rclpy.ok():
        rclpy.spin_once(node)  # サービスの処理待ち
        if future.done():  # サービスの処理が完了したか確認
            try:
                response = future.result()  # 結果を受け取り
            except Exception as e:
                node.get_logger().info('呼び出し失敗: {}'.format(e))
            else:
                node.get_logger().info("age: {}".format(response.age))
            break

    node.destroy_node()  # ノードの後始末
    rclpy.shutdown()     # ROS 2 シャットダウン

if __name__ == '__main__':
    main()

