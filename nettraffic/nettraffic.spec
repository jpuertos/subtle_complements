# -*- encoding: utf-8 -*-
# Nettraffic specification file
# Created with sur-0.2
Sur::Specification.new do |s|
  # Sublet information
  s.name        = "Nettraffic"
  s.version     = "1.0"
  s.tags        = [ ]
  s.files       = [ "nettraffic.rb" ]
  s.icons       = [ ]

  # Sublet description
  s.description = "Displays RX/TX speed."
  s.notes       = <<NOTES
LONG DESCRIPTION
NOTES

  # Sublet authors
  s.authors     = [ "Juan V. Puertos" ]
  s.contact     = "juanvi.puertos@gmail.com"
  s.date        = "Wed Jan 25 20:15 GMT 2012"

  # Sublet config
  #s.config = [
  #  {
  #    :name        => "Value name",
  #    :type        => "Value type",
  #    :description => "Description",
  #    :def_value   => "Default value"
  #  }
  #]

  # Sublet grabs
  #s.grabs = {
  #  :NettrafficGrab => "Sublet grab"
  #}

  # Sublet requirements
  # s.required_version = "0.9.2127"
  # s.add_dependency("subtle", "~> 0.1.2")
end
