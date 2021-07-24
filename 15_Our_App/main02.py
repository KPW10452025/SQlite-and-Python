import package

package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)

# Add many records
employee_list = [
    ('Aidan', 'Murphy', 'Aidan@gmail.con', 1, 296000),
    ('Scarlett', 'Landrum', 'Scarlett#gmail.com', 0 ,388000)
]
package.module.add_many(employee_list)
package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)
# (8, 'Aidan', 'Murphy', 'Aidan@gmail.con', 1, 296000)         <------- the new record
# (9, 'Scarlett', 'Landrum', 'Scarlett#gmail.com', 0, 388000)  <------- the new record

package.module.delete_one('8')
package.module.delete_one('9')
package.module.show_all()
# (1, 'Louis', 'Turner', 'Louis@gmail.com', 1, 238000)
# (2, 'Pete', 'Lyn Strong', 'Pete@gmail.com', 1, 305000)
# (3, 'Lizzie', 'Bowles', 'Lizzie@gmail.com', 0, 345000)
# (4, 'Kayla', 'Bowen', 'Kayla@gmail.com', 0, 465000)
# (5, 'Judy', 'Arnold\t', 'Judy@gmail.com', 0, 382000)
# (6, 'Marcus', 'Harper', 'Marcus@gmail.com', 1, 338000)
# (7, 'Brian', 'Williams', 'Brian@gmail.com', 1, 200000)
#                                                              <------- has been deleted
#                                                              <------- has been deleted
