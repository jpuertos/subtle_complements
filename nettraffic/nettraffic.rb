# Nettraffic sublet file
# Created with sur-0.2
helper do
  def read_byte_counters(iface_name)
    rx_bytes = 0
    tx_bytes = 0
    res = IO.readlines("/proc/net/dev")
    res.each do |l|
      if l.scan(iface_name).size == 1
        rx_bytes = l.split[1].to_i
        tx_bytes = l.split[9].to_i
        break
      end
    end
    return rx_bytes, tx_bytes
  end
end

configure :nettraffic do |s|
  s.interval = 1
  s.iface_name = s.config[:iface_name] || "eth0"
  s.last_counters = read_byte_counters(s.iface_name)
end

on :run do |s|
  current_counters = read_byte_counters(s.iface_name)
  rx_speed = (current_counters[0] - s.last_counters[0])/1000/s.interval
  tx_speed = (current_counters[1] - s.last_counters[1])/1000/s.interval
  s.last_counters = current_counters
  s.data = "D:#{rx_speed} KB/s U:#{tx_speed} KB/s"
end
